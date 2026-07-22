import os
from dotenv import load_dotenv

try:
    load_dotenv()
    MODEL_NAME = os.getenv("GOOGLE_GENAI_MODEL", "gemini-3.5-flash-lite")
except ImportError:
    print("Warning: Python-dotenv is not installed. Ensure GOOGLE_API_KEY is set.")
    MODEL_NAME = "ggemini-3.5-flash-lite"

from google.adk.agents import LlmAgent, SequentialAgent 
from google.adk.tools import google_search
from marketing_campaign_agent.instructions import MARKET_RESEARCH_INSTRUCTION, CAMPAIGN_ORCHESTRATOR_INSTRUCTION


market_research_agent = LlmAgent(
    name="MarketResearcher",
    model=MODEL_NAME,
    instruction=MARKET_RESEARCH_INSTRUCTION,
    tools=[google_search],
    output_key="market_research_summary"
)

campaign_orchestrator = SequentialAgent(
    name = "MarketingCampaignAssistant",
    description=CAMPAIGN_ORCHESTRATOR_INSTRUCTION,
    sub_agents= [market_research_agent]
)

root_agent = campaign_orchestrator