from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import requests
from bs4 import BeautifulSoup

class ScraperInput(BaseModel):
    url: str = Field(..., description="URL to scrape content from")

class WebScraperTool(BaseTool):
    name: str = "Web Scraper Tool"
    description: str = "Scrapes text content from a given URL."
    args_schema: type = ScraperInput

    def _run(self, url: str) -> str:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.get_text(separator=' ', strip=True)[:15000]
        except Exception as e:
            return f"Failed to scrape {url}: {e}"
