from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

for chunk in model.stream("Explain LangChain in simple words."):
    print(chunk.text, end="", flush=True)

print()