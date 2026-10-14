import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

async def main():
    questions = [
        "Explain RAG.",
        "Explain LangChain.",
        "Explain Agentic AI."
    ]

    responses = await asyncio.gather(
        *(model.ainvoke(question) for question in questions)
    )

    for question, response in zip(questions, responses):
        print(f"\nQuestion: {question}")
        print(f"Answer: {response.text}")

asyncio.run(main())