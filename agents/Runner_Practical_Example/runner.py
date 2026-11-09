import asyncio
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types
from agent import root_agent


from dotenv import load_dotenv
load_dotenv()


session_service_in_memory = InMemorySessionService()

initial_state = {
    "name": "Hrishi",
    "data": ("I am Hrishi, and I am a Software Engineer, with 11 years of experience in Python "
             "Backend development. I love Cricket, and my favourite player is Rohit Sharma.")
}

APP_NAME = "Hrishi_app"
USER_ID = "Hrishi"
SESSION_ID = "Hrishi_session"  # str(uuid.uuid4())


async def main():
    current_session = await session_service_in_memory.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        state=initial_state,
        session_id=SESSION_ID
    )

    print(f"Session created with {current_session.id}")

    created_sessions = await session_service_in_memory.list_sessions(
        app_name=APP_NAME,
        user_id=USER_ID
    )
    print(f"created_sessions: {created_sessions}")

    runner = Runner(
        agent=root_agent,
        session_service=session_service_in_memory,
        app_name=APP_NAME
    )

    new_message = types.Content(
        role="user",
        parts=[types.Part(text="Who is user favourite player?")]
    )

    for event in runner.run(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=new_message
    ):
        if event.is_final_response():
            print(f"event.content: {event.content}")
            if event.content and event.content.parts:
                print(f"final response: {event.content.parts[0].text}")


asyncio.run(main())
