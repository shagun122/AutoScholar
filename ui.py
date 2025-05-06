import streamlit as st
import asyncio
from data_loader import DataLoader
from ai_processor import AIProcessor
from llm_config import get_llm
from langchain_core.messages import SystemMessage, HumanMessage

st.set_page_config(page_title="📝 Research Paper Analyzer", layout="wide")

llm = get_llm()
data_loader = DataLoader()
ai_processor = AIProcessor(llm)

async def fetch_and_process_papers(query):
    papers = data_loader.fetch_arxiv_papers(query)
    if not papers:
        return []

    processed_papers = await ai_processor.process_papers_async(papers)
    return processed_papers

async def run_analysis_and_suggestions(query):
    papers = await fetch_and_process_papers(query)
    return papers

def main():
    st.title("📝 Research Paper Analyzer")
    query = st.text_input("🔍 Enter Search Query:", "")

    if st.button("🔄 Fetch & Analyze Papers"):
        with st.spinner("Fetching and processing papers..."):
            try:
                processed_papers = asyncio.run(run_analysis_and_suggestions(query))

                if not processed_papers:
                    st.warning("⚠️ No papers found. Try another query.")
                else:
                    for paper in processed_papers:
                        with st.expander(f"📄 {paper.get('title', 'N/A')}"): # Use .get for title
                            st.markdown(f"🔗 [Read more]({paper.get('link', '#')})", unsafe_allow_html=True) # Use .get for link
                            pdf_link = paper.get("pdf_link")
                            if pdf_link:
                                st.markdown(f" 📄 [Download PDF]({pdf_link})", unsafe_allow_html=True)

                            # Define the tab names explicitly
                            tab_names = ["Summary & Key Findings", "Trends", "Advantages & Disadvantages", "Related Work", "Code Implementations", "Citations & References", "Future Work"]
                            # Create the tabs and access by index
                            tabs = st.tabs(tab_names)

                            # Populate tabs using .get for safety and index access
                            with tabs[0]: # Summary & Key Findings
                                st.write("📌 **Summary:**")
                                st.info(paper.get("summary", "N/A"))
                                st.write("✨ **Key Findings:**")
                                st.info(paper.get("key_findings", "N/A"))

                            with tabs[1]: # Trends
                                st.write("📊 **Research Trends:**")
                                st.success(paper.get("trends", "N/A"))

                            with tabs[2]: # Advantages & Disadvantages
                                st.write("✅ **Advantages & Disadvantages:**")
                                st.warning(paper.get("advantages_disadvantages", "N/A"))

                            with tabs[3]: # Related Work
                                st.write("🤝 **Related Work:**")
                                st.info(paper.get("related_work", "N/A"))

                            with tabs[4]: # Code Implementations
                                st.write("💻 **Code Implementations:**")
                                st.code(paper.get("code_implementations", "N/A"), language="python")

                            with tabs[5]: # Citations & References
                                st.write("📖 **Citations & References:**")
                                st.code(paper.get("citations", "N/A"), language="markdown")

                            with tabs[6]: # Future Work
                                st.write("🔮 **Future Work:**")
                                st.info(paper.get("future_work", "N/A"))

            except Exception as e:
                st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
