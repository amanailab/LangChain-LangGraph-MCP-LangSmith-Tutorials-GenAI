# app.py
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# 1. Load variables from the .env file
load_dotenv()

# 2. Stop early with a clear message if the key is missing
if not os.getenv("GROQ_API_KEY"):
    raise SystemExit("GROQ_API_KEY is missing. Add it to your .env file.")

# 3. Create the chat model
model = ChatGroq(
model="openai/gpt-oss-20b",
temperature=0,
max_retries=2,
timeout=30,
)

# 4. Send one question to the model
response = model.invoke(
"Explain LangChain in simple English. "
"Give three bullet points and one practical example."
)


# 5. Print the answer text
print(response.text)