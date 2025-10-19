# from crewai.tools import SerpApiTool
# from config import SERPAPI_API_KEY

# class SerpSearchTool(SerpApiTool):
#     def __init__(self):
#         super().__init__(api_key=SERPAPI_API_KEY)


# from crewai import BaseTool
# import os
# import requests

# class SerpSearchTool(BaseTool):
#     name = "SerpAPI Search"
#     description = "Searches the web using SerpAPI for up-to-date information."

#     def _run(self, query: str) -> str:
#         api_key = os.getenv("SERPAPI_API_KEY")
#         if not api_key:
#             return "Missing SERPAPI_API_KEY in environment."

#         url = "https://serpapi.com/search"
#         params = {
#             "q": query,
#             "api_key": api_key,
#             "engine": "google",
#         }

#         response = requests.get(url, params=params)
#         if response.status_code != 200:
#             return f"Error fetching search results: {response.status_code}"

#         data = response.json()
#         # Try to get first organic result
#         try:
#             top_result = data.get("organic_results", [])[0]
#             return top_result.get("snippet", "No snippet available.")
#         except Exception as e:
#             return f"Failed to parse search results: {e}"


from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import requests
from config import SERPAPI_API_KEY

class SerpSearchInput(BaseModel):
    query: str = Field(..., description="Search query")

class SerpSearchTool(BaseTool):
    name: str = "SerpAPI Search Tool"
    description: str = "Searches the web using SerpAPI for relevant links"
    args_schema: type = SerpSearchInput


    def _run(self, query: str) -> str:
        try:
            url = "https://serpapi.com/search.json"
            params = {
                "q": query,
                "api_key": SERPAPI_API_KEY,
                "num": 5
            }
            response = requests.get(url, params=params)
            data = response.json()
            results = data.get("organic_results", [])
            return "\n".join([f"{res['title']}: {res['link']}" for res in results])
        except Exception as e:
            return f"Failed to fetch search results: {e}"
