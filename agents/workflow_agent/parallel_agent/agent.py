"""Sequential Agent Workflow example"""

from google.adk.agents.parallel_agent import ParallelAgent
from google.adk.agents import Agent


GEMINI_MODEL = "gemini-3.5-flash-lite"

def make_translator_agent(lang_code, output_key) -> Agent:
    return Agent(
        name=f"Translator_{lang_code}",
        model=GEMINI_MODEL,
        instruction=f"Translate the user_prompt into {lang_code}. "
                     "Return only the translation text.",
        output_key=output_key
    )


# Three independent translator
spanish = make_translator_agent(lang_code="Spanish", output_key="es")
french = make_translator_agent(lang_code="French", output_key="fr")
german = make_translator_agent(lang_code="German", output_key="de")
hindi = make_translator_agent(lang_code="Hindi", output_key="hn")


parallel_workflow = ParallelAgent(
    name="ParallelTranslate",
    sub_agents=[spanish, french, german, hindi],
    description="Runs three translate agents in Parallel."
)

root_agent = parallel_workflow
