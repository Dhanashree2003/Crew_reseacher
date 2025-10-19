# from crewai import Task
# from app.agents.scraper import scraper_agent

# scrape_extract_task = Task(
#     description=(
#         "Given the list of URLs per section/parameter (from the previous task), scrape the webpages and attempt to extract the content for each parameter of each section listed in {{ user_input.sections }}. "
#         "Only include content that is explicitly found. If a parameter cannot be found, set it to null. After extraction, apply retry logic: if the number of filled parameters in a section is below the minimum required threshold, trigger a retry loop."
#     ),
#     expected_output="Structured JSON: section → parameter → value/null",
#     agent=scraper_agent
# )
