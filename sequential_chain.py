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


summary_prompt = ChatPromptTemplate.from_template(
    "Summarize {topic} in two sentences."
)

summary_chain = summary_prompt | model | StrOutputParser()

print(summary_chain.invoke({"topic": "Machine Learning"}))