
from langchain.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# 1. Load variables from the .env file
load_dotenv()

# 3. Create the chat model
model = ChatGroq(
model="openai/gpt-oss-20b",
temperature=0,
max_retries=2,
timeout=30,
)

messages = [
    SystemMessage(
        content="You are a friendly Python instructor."
    ),
    HumanMessage(
        content="Explain Python dictionaries with an example."
    ),
]

response = model.invoke(messages)

print(response.text)
