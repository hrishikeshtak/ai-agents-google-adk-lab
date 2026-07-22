import os
from dotenv import load_dotenv
from google.adk.agents import Agent

try:
    load_dotenv()
    MODEL_NAME = os.getenv("GOOGLE_GENAI_MODEL", "gemini-3.5-flash-lite")
except ImportError:
    print("Warning: Python-dotenv is not installed. Ensure GOOGLE_API_KEY is set.")
    MODEL_NAME = "ggemini-3.5-flash-lite"


root_agent = Agent(
    name="assistant",
    model=MODEL_NAME,
    instruction="""
    You are a helpful Python assistant.
    Answer briefly.
    """
)
