from langchain_core.documents import Document

doc = Document(
    page_content="Refunds are allowed within 7 days of delivery.",
    metadata={
        "source": "refund_policy.txt",
        "topic": "refund"
    }
)

print(doc.page_content)
print(doc.metadata)