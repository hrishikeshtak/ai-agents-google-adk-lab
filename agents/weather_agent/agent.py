import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent


def get_weather(city: str) -> dict:
    """
    Retrieves a current weather report for a specified city.
    """

    if city.lower() == "new york":
        return {
            "status": "success",
            "report": ("The weather in new york is sunny with temperature of 35 degree "
            "celsius.")
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for city: {city} not available."
        }


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}


weather_agent = Agent(
    name="weather_time_agent",
    model="gemini-3.5-flash-lite",
    description=(
        "Agent to answer questions about the time and weather in a city."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about the time and weather in a "
        "city."
    ),
    tools=[get_weather, get_current_time],
)

root_agent = weather_agent
