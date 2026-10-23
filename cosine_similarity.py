from langchain_community.embeddings import FastEmbedEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding_model = FastEmbedEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)

texts = [
    "How can I request a refund?",
    "How do I get my money back?",
    "How do I reset my password?"
]

vectors = embedding_model.embed_documents(texts)

query_vector = embedding_model.embed_query(
    "I want to return my product and get my money back."
)

scores = cosine_similarity(
    [query_vector],
    vectors
)[0]

for text, score in sorted(
    zip(texts, scores),
    key=lambda item: item[1],
    reverse=True
):
    print(f"{score:.4f} | {text}")