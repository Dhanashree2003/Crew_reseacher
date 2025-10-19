# from crewai import Task
# from app.agents.url_fetcher import url_fetcher_agent

# fetch_urls_task = Task(
#     description=(
#         "You are to find URLs for the company '{{ company }}' and product '{{ product }}'. "
#         "For each section heading in '{{ sections }}', and each parameter underneath, fetch **trusted and relevant** URLs "
#         "that are likely to contain the required parameter-level content. "
#         "Return a dictionary structured as: section → parameter → list of {url, meta_description}."
#     ),
#     expected_output="Dictionary: section → parameter → list of URL and metadata",
#     agent=url_fetcher_agent
# )
