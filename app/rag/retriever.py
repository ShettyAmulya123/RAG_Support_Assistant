from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# STEP 1 — Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# STEP 2 — Load saved FAISS database
vectorstore = FAISS.load_local(
    "vectorstore",
    embedding_model,
    allow_dangerous_deserialization=True
)

# STEP 3 — Create retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

# STEP 4 — Test query
query = "How can I reset my password?"

# STEP 5 — Retrieve relevant chunks
results = retriever.invoke(query)

# STEP 6 — Print retrieved chunks
for i, doc in enumerate(results, start=1):
    print(f"\nResult {i}:\n")
    print(doc.page_content)
    print("-" * 50)