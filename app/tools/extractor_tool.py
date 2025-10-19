from crewai.tools import BaseTool
from pydantic import BaseModel, Field

class ExtractorInput(BaseModel):
    text: str = Field(..., description="Text to extract from")
    parameter: str = Field(..., description="Parameter to find in text")

class ContentExtractorTool(BaseTool):
    name: str = "Content Extractor Tool"
    description: str = "Extracts parameter-specific content from scraped text"
    args_schema: type = ExtractorInput

    def _run(self, text: str, parameter: str) -> str:
        param_lower = parameter.lower()
        text_lower = text.lower()
        if param_lower in text_lower:
            idx = text_lower.find(param_lower)
            snippet = text[idx: idx + 400]
            return snippet.strip()
        else:
            return None
