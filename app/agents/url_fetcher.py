from crewai import Agent
from app.llm.gemini_llm import gemini_llm
from app.tools.serp_api_tool import SerpSearchTool


url_fetcher_agent = Agent(
    role="Web URL Fetcher",
    goal="Given company, product and sections+parameters, fetch trustworthy URLs for each section heading.",
    backstory="Expert researcher sourcing high-quality sources from the web.",
    tools=[SerpSearchTool()],
    llm=gemini_llm, 
    verbose=True
)
