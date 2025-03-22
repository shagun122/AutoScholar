import asyncio
from agents import ResearchAgent

class AIProcessor:
    def __init__(self, llm):
        self.agent = ResearchAgent(llm)

    async def process_papers_async(self, papers):
        tasks = [self.agent.process_paper_async(paper) for paper in papers]
        return await asyncio.gather(*tasks)
