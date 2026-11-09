"""
Customer Support (Travel) - Multi Agent

This code defines a multi agent for Travel customer support scenarios.
    - Functions: check_order_status, lookup_product_info
    - Agents: order_agent, product_agent, search_agent, root_agent
    - Tools on root: AgentTool(search_agent), check_order_status
"""


from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool


def check_order_status(order_id: str) -> dict:
    """
    Return a status of travel booking (PNR/Reference).

    Input:
        order_id (str): Booking reference (e.g. 'PUN123')

    Output (dict):
        {
            "order_id": str,
            "status": str,      # e.g. "Ticketed", "Awaited Payment", "Completed", "Not Found"
            "pnr": str | None   # booking PNR if Ticketed
            "from": str | None  # origin of ticket
            "to": str | None    # destination of ticket
            "departure": str    # ISO Date of departure or unknown
        }
    """
    print(f"Checking order status of {order_id}")

    # Mock booking store
    bookings = {
        "PUN123": {
            "status": "Ticketed",
            "pnr": "PNR123",
            "departure": "2026-11-15",
            "from": "Pune",
            "to": "Bali"
        },
        "DUB123": {
            "status": "Awaited Payment",
            "pnr": None,
            "departure": "2026-11-25",
            "from": "Mumbai",
            "to": "Dubai"
        },
        "TY0777": {
            "status": "Completed",
            "pnr": "PNR321",
            "departure": "2025-08-31",
            "from": "Mumbai",
            "to": "Hyderabad"
        },
        "BL456": {
            "status": "Ticketed",
            "pnr": "PNR456",
            "departure": "2026-12-10",
            "from": "Mumbai",
            "to": "Bali"
        },
        "MAL789": {
            "status": "Pending Confirmation",
            "pnr": None,
            "departure": "2026-12-20",
            "from": "Delhi",
            "to": "Maldives"
        },
        "THA234": {
            "status": "Cancelled",
            "pnr": None,
            "departure": "2026-11-18",
            "from": "Pune",
            "to": "Thailand"
        },
        "SIN567": {
            "status": "Ticketed",
            "pnr": "PNR567",
            "departure": "2027-01-05",
            "from": "Mumbai",
            "to": "Singapore"
        },
        "GOA111": {
            "status": "Awaited Payment",
            "pnr": None,
            "departure": "2026-11-05",
            "from": "Pune",
            "to": "Goa"
        },
        "EUR999": {
            "status": "Ticketed",
            "pnr": "PNR999",
            "departure": "2027-04-12",
            "from": "Mumbai",
            "to": "Paris"
        },
        "PUN555": {
            "status": "Completed",
            "pnr": "PNR555",
            "departure": "2026-06-15",
            "from": "Pune",
            "to": "Dubai"
        }
}

    if order_id in bookings:
        info = {"order_id": order_id, **bookings[order_id]}
    else:
        info = {"order_id": order_id, "status": "Not Found", "pnr": None, "departure": None, "from": None, "to": None}

    return info


def lookup_product_info(product_name: str) -> dict:
    """
    Return destination/package info such as price, availability, seasons, and highlights.

    Input:
        product_name (str): destination or package name (e.g. "Dubai")

    Output (dict):
        "name": str,
        "avg_price": str,       # display-friendly price range
        "availability": str     # open, limited, seasonal, not listed
        "best_season": str      # human friendly season guidance
        "highlights": list      # short bullets of attractions or features
    """

    print(f"destination lookup up: {product_name}")

    # Mock Catalog
    catalog = {
        "bali": {
            "name": "Bali Indonesia Holiday Package",
            "avg_price": "₹65,000 - ₹95,000 per person",
            "availability": "open",
            "best_season": "April to October (Dry Season)",
            "highlights": [
                "Visit Ubud Monkey Forest and Tegallalang Rice Terraces",
                "Explore Tanah Lot Temple",
                "Enjoy sunset at Uluwatu Temple",
                "Relax at Seminyak and Kuta beaches",
                "Experience traditional Balinese spa and culture"
            ]
        },
        "dubai": {
            "name": "Dubai & Abu Dhabi Holiday Package",
            "avg_price": "₹55,000 - ₹85,000 per person",
            "availability": "open",
            "best_season": "November to March (Pleasant Weather)",
            "highlights": [
                "Visit Burj Khalifa observation deck",
                "Enjoy Dubai Desert Safari with BBQ dinner",
                "Explore Dubai Mall and Dubai Fountain",
                "Visit Sheikh Zayed Grand Mosque in Abu Dhabi",
                "Experience Ferrari World or Warner Bros World"
            ]
        },
        "maldives": {
            "name": "Maldives Luxury Island Escape",
            "avg_price": "₹85,000 - ₹1,50,000 per person",
            "availability": "limited",
            "best_season": "November to April (Dry Season)",
            "highlights": [
                "Stay in luxury overwater villas",
                "Enjoy snorkeling and scuba diving",
                "Experience private island dining",
                "Explore marine life and coral reefs",
                "Enjoy sunset dolphin cruise"
            ]
        },
        "thailand": {
            "name": "Thailand Bangkok & Phuket Holiday",
            "avg_price": "₹45,000 - ₹75,000 per person",
            "availability": "open",
            "best_season": "November to February (Cool and Dry Season)",
            "highlights": [
                "Explore Bangkok temples and floating markets",
                "Enjoy Phuket beaches and island hopping",
                "Visit Phi Phi Islands",
                "Experience Thai cultural shows",
                "Explore local street food and night markets"
            ]
        },
        "singapore": {
            "name": "Singapore Family Holiday Package",
            "avg_price": "₹70,000 - ₹1,10,000 per person",
            "availability": "seasonal",
            "best_season": "February to April (Generally Pleasant Weather)",
            "highlights": [
                "Visit Universal Studios Singapore",
                "Explore Gardens by the Bay",
                "Enjoy Marina Bay Sands SkyPark",
                "Visit Singapore Zoo and Night Safari",
                "Experience Sentosa Island attractions"
            ]
        }
    }

    key = product_name.lower().strip()
    if key in catalog:
        info = {**catalog[key]}
    else:
        info = {"name": product_name, 
                "avg_price": "Unknown", 
                "availability": "Not Listed", 
                "best_season": "varies",
                "highlights": []
            }

    return info


order_agent = Agent(
    name="order_agent",
    model="gemini-3.5-flash-lite",
    description="I handle all booking related enquiries and trackings.",  # clear description helps routing
    instruction="""
    You are a travel booking specialists. When customer ask about bookings:

    1. Use check_order_status to retrieve booking info (status, pnr, route, date).
    2. Give clear updates and next steps (payment, documents, recheck time).
    3. If ticketed share PNR and departure. If pending, explain what is needed.

    Be friendly and precise.
    Example: "Your booking NYC123 is ticketed. PNR PNR789 for JFK -> LHR on 2025-09-15."

    After your answer, return control to customer support manager.
    """,
    tools=[check_order_status],
)

product_agent = Agent(
    name="product_agent",
    model="gemini-3.5-flash-lite",
    description="I help with destination or package information and availability.",  # clear description helps routing
    instruction="""
    You are a destination/package specialists. When customer ask about travel options:

    1. Use lookup_product_info to fetch details.
    2. Share price range, availabilty, best seaons, and highlights.
    3. Suggest nearby or similar options when availability is limited.

    Be helpful and travel-savvy.

    After your answer, return control to customer support manager.
    """,
    tools=[lookup_product_info],
)

search_agent = Agent(
    name="search_agent",
    model="gemini-3.5-flash-lite",
    description="I help with general travel questions and quick lookups.",  # clear description helps routing
    instruction="""
    You are a general travel support specialists. For broad questions:

    1. Provide clear guidance, (baggage policy, visa notes, airport tags)
    2. Use web search when current information is required.
    3. If unsure, recommend checking official sources.
    """,
    tools=[google_search],
)

root_agent = Agent(
    name="customer_service_manager",
    model="gemini-3.5-flash-lite",
    description="I am travel service manager, who co-ordinates all enquiries.",
    instruction="""
    You are a travel service manager. Route customer requests to the right specialist:

    - Booking questions (PNR, status, dates): call the check_order_status tool.
    - Destination/package questions (price, availability, highlights) deletegate to product_agent
    - General travel enquiries (policies, news): use search_agent via AgentTool

    Be professional and ensure each answer is accurate and complete. 
    """,
    sub_agents=[product_agent],
    tools=[AgentTool(search_agent), check_order_status]
)
