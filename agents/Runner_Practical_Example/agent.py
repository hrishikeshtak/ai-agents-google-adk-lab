from google.adk.agents import Agent
from dotenv import load_dotenv

load_dotenv()


root_agent = Agent(
    name="planner_agent",
    model="gemini-3.5-flash-lite",
    description="A helpful assistant to user questions.",
    instruction=(
        "Answer user questions to the best of your knowledge. "
        "You might have to answer questions about the use, their interestes, their preferences."
        "You can access the same for user {name} in the session state."
        "and the data information is {data}"
    )
)
