from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


openai_model = LiteLlm(model="openai/gpt-4o")


agent_openai = Agent(
    model=openai_model,
    name="openai_agent",
    instruction="You are a helpful assistant powered by GPT-4o.",
    # ... other agent parameters
)

root_agent = agent_openai
