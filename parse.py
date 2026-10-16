from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

result = parser.invoke("Hello from LangChain!")

print(result)
print(type(result))



from langchain_core.output_parsers import CommaSeparatedListOutputParser

parser = CommaSeparatedListOutputParser()

result = parser.invoke("Python, Java, C++")

print(result)




from langchain_core.output_parsers import JsonOutputParser

parser = JsonOutputParser()

result = parser.invoke(
    '{"name": "Aman", "skill": "AI"}'
)

print(result["name"])
print(result["skill"])