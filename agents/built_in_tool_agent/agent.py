from google.adk.agents import Agent
from google.adk.tools import google_search, AgentTool
import math


def calculate_area(shape: str, value: float) -> dict:
    """
    Calculate the area of the given shape

    Args:
        shape (str): The type of shape ("circle" or "square")
        value (float): The radius (circle) or side length (square)
    
    Returns:
        dict: status and result or error message
    """

    if shape.lower() == "circle":
        area = math.pi * value * value
        return {"status": "success", "report": f"The area of circle is {area:.2f}"}
    elif shape.lower() == "square":
        area = value * value
        return {"status": "success", "report": f"The area of square is {area:.2f}"}
    return {"status": "error", "error_message": f"Sorry, I can only calculate area of circle or square, not for {shape}"}


search_agent = Agent(
    name="search_agent",
    model="gemini-3.5-flash-lite",
    tools=[google_search],
    description="An assistant that helps with query search on internet when needed",
    instruction=("You are a helpful search assistant. When the user asks about current event or"
    "factual information, use google_search tool. Always return a clear and short description.")
)

search_agent_tool = AgentTool(search_agent)

root_agent = Agent(
    name="area_agent",
    model="gemini-3.5-flash-lite",
    tools=[calculate_area, search_agent_tool],
    description="An assistant that helps with simple math problem",
    instruction=("You are a helpful math assistant. When the user asks about area of circle or " \
    "square shape use calculate_area tool. Always return a clear and short description.")
)
