from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Explain {topic} in simple language."
)

result = prompt.invoke({"topic": "RAG"})

print(result.to_string())