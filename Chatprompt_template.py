from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI teacher."),
    ("human", "Explain {topic} with one example.")
])

messages = prompt.invoke({"topic": "LangChain"})

print(messages.to_messages())