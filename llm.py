import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_model():
    if not os.getenv("GROQ_API_KEY"):
        raise RuntimeError("GROQ_API_KEY is missing")

    return ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0
    )