from fastapi import FastAPI
from pydantic import BaseModel
from app.crew_config import run_crew
from app.retry_logic import is_section_valid

app = FastAPI()

DEFAULT_PARAMETERS = {
    "Capabilities & Limits": ["Topic", "Capabilities","Limitations","notes"],
    "ExecAndQuestions": ["Topic", "executive summary 200 words", "Key questions answered","citations","notes"],
    
}

class UserInput(BaseModel):
    company: str
    product: str
    sections: list[str]

@app.post("/generate-report")
async def generate_report(input: UserInput):
    sections_selected = {sec: DEFAULT_PARAMETERS[sec] for sec in input.sections if sec in DEFAULT_PARAMETERS}
    user_input = {
        "company": input.company,
        "product": input.product,
        "sections": sections_selected
    }

    extracted_data = run_crew(user_input)

    if not is_section_valid(extracted_data, min_required_per_section=2):
        return {"error": "Not enough data extracted for one or more sections. Please retry."}

    return {"report_data": extracted_data}
