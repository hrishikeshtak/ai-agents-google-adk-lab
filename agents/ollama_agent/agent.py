from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm


ollama_model = LiteLlm(model="ollama_chat/llama3.2")

agent_ollama = Agent(
    model=ollama_model,
    name="ollama_agent",
    description="A helpful assistant for user questions.",
    instruction="You are an assistant powered by Ollama model."
)

root_agent = agent_ollama
