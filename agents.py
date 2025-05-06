import asyncio
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

class ResearchAgent:
    def __init__(self, llm):
        self.llm = llm

    async def summarize_paper(self, paper):
        messages = [
            SystemMessage(content="Provide a concise yet comprehensive academic summary of the following research paper, highlighting key findings, methodology, and contributions to the field:"),
            HumanMessage(content=paper["summary"])
        ]
        response = await self.llm.ainvoke(messages)
        return response.content.strip()

    async def extract_key_findings(self, paper):
        messages = [
            SystemMessage(content="List the main findings, results, and conclusions of this research paper in a clear, concise bulleted format:"),
            HumanMessage(content=paper["summary"])
        ]
        response = await self.llm.ainvoke(messages)
        return response.content.strip()

    async def analyze_trends(self, paper):
        messages = [
            SystemMessage(content="Analyze current and emerging research trends related to this paper's field. Explain their significance and cite potential future directions, referencing relevant works where possible:"),
            HumanMessage(content=paper["summary"])
        ]
        response = await self.llm.ainvoke(messages)
        return response.content.strip()

    async def extract_adv_dis(self, paper):
        messages = [
            SystemMessage(content="Critically evaluate the strengths (e.g., methodological rigor, novelty) and limitations (e.g., scope, assumptions) of this research paper in a structured format (e.g., bullet points):"),
            HumanMessage(content=paper["summary"])
        ]
        response = await self.llm.ainvoke(messages)
        return response.content.strip()

    async def analyze_related_work(self, paper):
        messages = [
            SystemMessage(content="Analyze how this paper relates to other significant works mentioned in its introduction or related work section. Describe its position within the broader research landscape:"),
            HumanMessage(content=paper["summary"])
        ]
        response = await self.llm.ainvoke(messages)
        return response.content.strip()

    async def extract_citations(self, paper):
        messages = [
            SystemMessage(content="Identify and list the seminal works and highly relevant recent citations related to this paper, providing context for their importance:"),
            HumanMessage(content=paper["summary"])
        ]
        response = await self.llm.ainvoke(messages)
        return response.content.strip()

    async def suggest_code_implementations(self, paper):
        messages = [
            SystemMessage(content="Propose relevant algorithms, libraries, or pseudocode based on this research paper's technical contributions, suitable for practical application or further development:"),
            HumanMessage(content=paper["summary"])
        ]
        response = await self.llm.ainvoke(messages)
        return response.content.strip()

    async def suggest_future_work(self, paper):
        messages = [
            SystemMessage(content="Based on the paper's discussion and conclusion, identify and suggest potential future research directions, open questions, or next steps:"),
            HumanMessage(content=paper["summary"])
        ]
        response = await self.llm.ainvoke(messages)
        return response.content.strip()

    async def process_paper_async(self, paper):
        summary = await self.summarize_paper(paper)
        key_findings = await self.extract_key_findings(paper)
        trends = await self.analyze_trends(paper)
        advantages_disadvantages = await self.extract_adv_dis(paper)
        related_work = await self.analyze_related_work(paper)
        citations = await self.extract_citations(paper)
        code_implementations = await self.suggest_code_implementations(paper)
        future_work = await self.suggest_future_work(paper)

        return {
            "title": paper["title"],
            "link": paper["link"],
            "summary": summary,
            "key_findings": key_findings,
            "trends": trends,
            "advantages_disadvantages": advantages_disadvantages,
            "related_work": related_work,
            "citations": citations,
            "code_implementations": code_implementations,
            "future_work": future_work
        }
