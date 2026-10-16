from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
model="openai/gpt-oss-20b",
temperature=0,
max_retries=2,
timeout=30,
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Use the supplied history."),
    MessagesPlaceholder("history", optional=True),
    ("human", "{question}")
])

chat_chain = prompt | model | StrOutputParser()

history = []

question = "My name is Rahul."
answer = chat_chain.invoke({
    "history": history,
    "question": question
})

history.extend([
    HumanMessage(content=question),
    AIMessage(content=answer)
])

question = "What is my name?"
answer = chat_chain.invoke({
    "history": history,
    "question": question
})

print(answer)

history.extend([
    HumanMessage(content=question),
    AIMessage(content=answer)
])