import asyncio
from langchain_core.prompts import ChatPromptTemplate

class ResearchAgent:
    def __init__(self, llm):
        self.llm = llm  # Groq LLM instance

    async def summarize_paper(self, paper):
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Summarize the following research paper in simple, clear terms for a general audience:"),
            ("user", paper["summary"])
        ])
        response = await self.llm.ainvoke(prompt.format_messages())
        return response.content.strip()

    async def analyze_trends(self, paper):
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Identify and explain major research trends related to this paper in easy-to-understand terms."),
            ("user", paper["summary"])
        ])
        response = await self.llm.ainvoke(prompt.format_messages())
        return response.content.strip()

    async def extract_adv_dis(self, paper):
        prompt = ChatPromptTemplate.from_messages([
            ("system", "List the key advantages and disadvantages of this research paper in a structured format:"),
            ("user", paper["summary"])
        ])
        response = await self.llm.ainvoke(prompt.format_messages())
        return response.content.strip()

    async def extract_citations(self, paper):
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Find and list the most relevant citations and references related to this paper."),
            ("user", paper["summary"])
        ])
        response = await self.llm.ainvoke(prompt.format_messages())
        return response.content.strip()

    async def suggest_code_implementations(self, paper):
        prompt = ChatPromptTemplate.from_messages([
            ("system", "Suggest practical code implementations based on this research paper."),
            ("user", paper["summary"])
        ])
        response = await self.llm.ainvoke(prompt.format_messages())
        return response.content.strip()

    async def process_paper_async(self, paper):
        tasks = [
            self.summarize_paper(paper),
            self.analyze_trends(paper),
            self.extract_adv_dis(paper),
            self.extract_citations(paper),
            self.suggest_code_implementations(paper)
        ]
        results = await asyncio.gather(*tasks)

        return {
            "title": paper["title"],
            "link": paper["link"],
            "summary": results[0],
            "trends": results[1],
            "advantages_disadvantages": results[2],
            "citations": results[3],
            "code_implementations": results[4]
        }