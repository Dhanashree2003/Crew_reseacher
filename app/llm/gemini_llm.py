import os
from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

gemini_llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY"),  # or replace with a direct string for quick test
    temperature=0.5
)

# import os
# from dotenv import load_dotenv
# from crewai import LLM  # assuming crewai is installed and imported

# load_dotenv()

# class GeminiLLMWrapper:
#     def __init__(self):
#         self.api_key = os.getenv("GEMINI_API_KEY")
#         self.temperature = 0.5
#         # Initialize the LLM directly, no self.client
#         self.llm = LLM(
#             model="gemini/gemini-2.0-flash",
#             api_key=self.api_key,
#             temperature=self.temperature
#         )

#     def call(self, messages, **kwargs):
#         try:
#             # Prepare prompt from messages
#             prompt = "\n".join([msg["content"] for msg in messages])
#             print("🔍 Prompt sent to Gemini (first 500 chars):", prompt[:500])

#             # Call the LLM with the prompt
#             response = self.llm(prompt, **kwargs)

#             # Check for empty or invalid response
#             if not response or 'output' not in response or not response['output']:
#                 raise ValueError("Empty response from Gemini")

#             return {"output": response["output"].strip()}

#         except Exception as e:
#             print("❌ Gemini LLM Error:", e)

#             # Fallback logic: You can customize what fallback to do here
#             # For example, return a default message or call another model

#             fallback_message = "Sorry, the LLM is currently unavailable. Please try again later."
#             return {"output": fallback_message}
