# direct_groq.py (comparison only: the same request without LangChain)
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

completion = client.chat.completions.create(
model="openai/gpt-oss-20b",
messages=[
{"role": "system", "content": "You are a helpful tutor."},
{"role": "user", "content": "Explain LangChain in one sentence."},
],
temperature=0,
)


print(completion.choices[0].message.content)