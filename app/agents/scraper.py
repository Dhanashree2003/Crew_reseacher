from crewai import Agent
from app.llm.gemini_llm import gemini_llm
from app.tools.scraper_tool import WebScraperTool
from app.tools.extractor_tool import ContentExtractorTool
# from app.llm.gemini_llm import GeminiLLMWrapper
# gemini_llm = GeminiLLMWrapper()

scraper_agent = Agent(
    role="Web Content Scraper & Extractor",
    goal="Using the fetched URLs, scrape the pages and extract content for each section’s parameters. Do not assume content — if you cannot find a parameter, it must be null.",
    backstory="Analyst who scrapes, parses and aligns content to structured parameters.",
    tools=[WebScraperTool(), ContentExtractorTool()],
    llm=gemini_llm,
    verbose=True
)
