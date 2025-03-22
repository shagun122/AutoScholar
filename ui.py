import streamlit as st
import asyncio
from data_loader import DataLoader
from ai_processor import AIProcessor
from llm_config import get_llm

st.set_page_config(page_title="📝 Research Paper Analyzer", layout="wide")

llm = get_llm()
data_loader = DataLoader()
ai_processor = AIProcessor(llm)

async def fetch_and_process_papers(query):
    papers = data_loader.fetch_arxiv_papers(query)
    if not papers:
        return []

    loop = asyncio.get_running_loop()
    processed_papers = await ai_processor.process_papers_async(papers)
    return processed_papers

def main():
    st.title("📝 Research Paper Analyzer")
    query = st.text_input("🔍 Enter Search Query:", "")

    if st.button("🔄 Fetch & Analyze Papers"):
        with st.spinner("Fetching and processing papers..."):
            processed_papers = asyncio.run(fetch_and_process_papers(query))

            if not processed_papers:
                st.warning("⚠️ No papers found. Try another query.")
            else:
                for paper in processed_papers:
                    st.subheader(f"📄 {paper['title']}")
                    st.markdown(f"🔗 [Read more]({paper['link']})", unsafe_allow_html=True)
                    
                    st.write("📌 **Summary:**")
                    st.info(paper["summary"])
                    
                    st.write("📊 **Research Trends:**")
                    st.success(paper["trends"])
                    
                    st.write("✅ **Advantages & Disadvantages:**")
                    st.warning(paper["advantages_disadvantages"])
                    
                    st.write("📖 **Citations & References:**")
                    st.code(paper["citations"], language="markdown")
                    
                    st.write("💻 **Code Implementations:**")
                    st.code(paper["code_implementations"], language="python")

if __name__ == "__main__":
    main()
