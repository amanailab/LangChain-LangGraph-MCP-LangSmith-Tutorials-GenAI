
from langchain.messages import SystemMessage, HumanMessage
from llm import get_model
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



history = [
    SystemMessage(
        content="You are a concise Python tutor."
    )
]


def ask(question):
    history.append(HumanMessage(content=question))

    response = model.invoke(history)

    history.append(response)

    return response.text


print(ask("My favourite language is Python."))
print(ask("Which language did I mention?"))
