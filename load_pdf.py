from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("data/AmanAI_LangChain_Video3_Notes.pdf")
documents = loader.load()

print("Pages:", len(documents))

for doc in documents[:2]:
    print("Content:", doc.page_content[:200])
    print("Metadata:", doc.metadata)