from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# STEP 1 — Load PDF
loader = PyPDFLoader("data/knowledge_base.pdf")
documents = loader.load()

print(f"Loaded {len(documents)} pages")

# STEP 2 — Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")

# STEP 3 — Create embeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# STEP 4 — Store in FAISS
vectorstore = FAISS.from_documents(
    chunks,
    embedding_model
)

vectorstore.save_local("vectorstore")

print("FAISS vector store created successfully")