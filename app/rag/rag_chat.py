from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from app.rag.llm import generate_answer

# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database
vectorstore = FAISS.load_local(
    "vectorstore",
    embedding_model,
    allow_dangerous_deserialization=True
)

# Create retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

# User query
query = input("Ask your question: ")

# Retrieve relevant chunks
docs = retriever.invoke(query)

# Combine retrieved context
context = "\n".join([
    doc.page_content for doc in docs
])

# Generate final answer
answer = generate_answer(query, context)

print("\nAI Response:\n")
print(answer)