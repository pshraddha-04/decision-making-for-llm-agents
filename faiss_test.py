from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

chunks = [
    "The Eiffel Tower is located in Paris, France.",
    "Machine learning is a subset of artificial intelligence.",
    "Python is a popular programming language for data science.",
    "The Amazon River is the largest river by discharge in the world.",
    "Neural networks are inspired by the human brain.",
    "FastAPI is a modern web framework for building APIs with Python.",
]

print("Loading embedding model...")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

print("Indexing chunks into FAISS...")
vectorstore = FAISS.from_texts(chunks, embeddings)

query = "What programming language is used for data science?"
print(f"\nQuery: {query}")

results = vectorstore.similarity_search(query, k=2)
print("\nTop 2 results:")
for i, doc in enumerate(results, 1):
    print(f"  {i}. {doc.page_content}")
