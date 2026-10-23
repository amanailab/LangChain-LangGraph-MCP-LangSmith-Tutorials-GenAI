from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

documents = [
    Document(
        page_content=(
            "Refunds are allowed within 7 days of delivery. "
            "Items must be unused and in original packaging. "
            "Damaged items must be reported within 48 hours."
        ),
        metadata={"source": "refund_policy.txt"}
    )
]

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_documents(documents)

print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}:")
    print(chunk.page_content)
    print(chunk.metadata)