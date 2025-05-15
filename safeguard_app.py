
import streamlit as st
from langchain.llms import Ollama
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
from langchain.tools import Tool

# Counter file
COUNTER_FILE = "visit_counter.txt"

def increment_counter():
    try:
        with open(COUNTER_FILE, "r") as file:
            count = int(file.read().strip())
    except:
        count = 0
    count += 1
    with open(COUNTER_FILE, "w") as file:
        file.write(str(count))
    return count

def get_visit_count():
    try:
        with open(COUNTER_FILE, "r") as file:
            return int(file.read().strip())
    except:
        return 0

# Tools
def crime_check_tool(query: str) -> str:
    dummy_data = {
        "new york": "High risk in areas like Bronx and certain subway lines.",
        "chicago": "Caution advised in South Side; some gang activity.",
        "los angeles": "Some theft reported in Skid Row and DTLA areas.",
        "your city": "No specific data, but always stay aware of surroundings."
    }
    for location in dummy_data:
        if location in query.lower():
            return dummy_data[location]
    return "No known risks found, but always use general caution."

tools = [
    Tool(name="CrimeDataChecker", func=crime_check_tool, description="Use to check crime risk in any location or city.")
]

llm = Ollama(model="llama3")

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Streamlit UI
st.set_page_config(page_title="SafeRoute AI", layout="centered")

st.title("SafeRoute AI Agent")
st.markdown("Check route safety using local AI. Powered by LLaMA 3 and LangChain.")

visit_count = increment_counter()
st.markdown(f"**Total users so far:** {visit_count}")

user_input = st.text_input("Enter your route or location (e.g., 'I'm going from Brooklyn to Manhattan'):")

if user_input:
    with st.spinner("Analyzing route..."):
        response = agent.run(user_input)
    st.success("Here's your safety insight:")
    st.write(response)
