from langchain_core.runnables import RunnableParallel
from langchain_core.prompts import ChatPromptTemplate
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

summary = (
    ChatPromptTemplate.from_template(
        "Summarize {topic} in one sentence."
    )
    | model
    | StrOutputParser()
)

key_points = (
    ChatPromptTemplate.from_template(
        "Give three key points about {topic}."
    )
    | model
    | StrOutputParser()
)

parallel_chain = RunnableParallel(
    summary=summary,
    key_points=key_points
)

result = parallel_chain.invoke({"topic": "RAG"})

print(result["summary"])
print(result["key_points"])