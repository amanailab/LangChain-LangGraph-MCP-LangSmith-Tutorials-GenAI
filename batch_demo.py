from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

questions = [
    "Explain RAG in simple words.",
    "Explain LangChain in simple words.",
    "Explain Agentic AI in simple words."
]

responses = model.batch(questions)

for question, response in zip(questions, responses):
    print("\nQuestion:", question)
    print("Answer:", response.text)