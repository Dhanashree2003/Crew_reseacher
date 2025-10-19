from crewai import Crew, Task
from app.agents.url_fetcher import url_fetcher_agent
from app.agents.scraper import scraper_agent
from app.llm.gemini_llm import gemini_llm
# from app.llm.gemini_llm import GeminiLLMWrapper
# gemini_llm = GeminiLLMWrapper()


def run_crew(user_input: dict) -> dict:
    fetch_urls_task = Task(
        description=(
            f"You are to find URLs for the company '{user_input['company']}' and product '{user_input['product']}'. "
            f"For each section heading in {list(user_input['sections'].keys())}, and each parameter underneath, "
            "fetch **trusted and relevant** URLs that are likely to contain the required parameter‑level content. "
            "Return a dictionary structured as: section → parameter → list of {url, meta_description}."
        ),
        expected_output="Dictionary: section → parameter → list of URL and metadata",
        agent=url_fetcher_agent
    )

    scrape_extract_task = Task(
    description=(
        "Given the list of URLs per section/parameter (from the previous task), scrape the webpages and attempt to extract the content for each parameter of each section listed in {{ user_input.sections }}. "
        "Only include content that is explicitly found. If a parameter cannot be found, set it to null. After extraction, apply retry logic: if the number of filled parameters in a section is below the minimum required threshold, trigger a retry loop."
    ),
    expected_output="Structured JSON: section → parameter → value/null",
    agent=scraper_agent
    )

    crew = Crew(
        agents=[url_fetcher_agent, scraper_agent],
        tasks=[fetch_urls_task, scrape_extract_task],
        llm=gemini_llm,
        verbose=True
    )

    result = crew.kickoff()
    return result
