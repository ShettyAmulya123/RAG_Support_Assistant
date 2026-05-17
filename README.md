# 🤖 RAG-Based Customer Support Assistant

An AI-powered Customer Support Assistant built using Retrieval-Augmented Generation (RAG) architecture with LangChain, LangGraph, FAISS, FastAPI, and Streamlit.

The system retrieves relevant information from a company knowledge base PDF and generates grounded responses using Groq Llama 3.3 LLM.

---

# 🚀 Features

- PDF-based knowledge ingestion
- Semantic search using vector embeddings
- FAISS vector database integration
- Retrieval-Augmented Generation (RAG)
- Workflow orchestration using LangGraph
- FastAPI backend APIs
- Streamlit chatbot UI
- Logging and request tracing
- Prometheus metrics monitoring
- Modular project architecture

---

# 🏗️ Project Architecture :

```text

User Query
    ↓
Streamlit Frontend
    ↓
FastAPI Backend
    ↓
LangGraph Workflow
    ↓
Retriever (FAISS)
    ↓
Relevant Context
    ↓
Groq LLM
    ↓
AI Response



🛠️ Technology :

| Technology             | Purpose                              |
| ---------------------- | ------------------------------------ |
| Python                 | Core programming language            |
| LangChain              | RAG pipeline and document processing |
| LangGraph              | Workflow orchestration               |
| FAISS                  | Vector database                      |
| HuggingFace Embeddings | Semantic embeddings                  |
| Groq Llama 3.3         | LLM response generation              |
| FastAPI                | Backend API framework                |
| Streamlit              | Frontend UI                          |
| Prometheus             | Metrics monitoring                   |
| Logging                | Application observability            |


📂 Project Structure

rag-support-assistant/
│
├── app/
│   ├── rag/
│   │   ├── ingest.py
│   │   ├── retriever.py
│   │   ├── llm.py
│   │   ├── graph.py
│   │   └── rag_chat.py
│   │
│   ├── api.py
│   ├── ui.py
│   ├── logging_config.py
│   └── metrics.py
│
├── data/
│   └── knowledge_base.pdf
│
├── vectorstore/
│
├── logs/
│   └── app.log
│
├── requirements.txt
├── .env
└── README.md


⚙️ Installation
1️⃣ Clone Repository
git clone <your-github-repo-link>

cd rag-support-assistant
2️⃣ Create Virtual Environment
python -m venv venv

Activate Environment
Windows: venv\Scripts\activate
Linux / Mac: source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt
🔑 Environment Variables

Create a .env file in the project root:
GROQ_API_KEY=your_groq_api_key

📄 Knowledge Base Ingestion
Place your PDF inside: data/
Run ingestion pipeline: python -m app.rag.ingest
This performs:
PDF loading
chunking
embeddings generation
FAISS vector storage

🚀 Run FastAPI Backend
uvicorn app.api:api --reload
Backend runs at: http://127.0.0.1:8000

Swagger API Docs: http://127.0.0.1:8000/docs

💬 Run Streamlit Frontend
Open another terminal: streamlit run app/ui.py

Frontend runs at: http://localhost:8501

📊 Metrics Endpoint
Prometheus metrics available at: http://127.0.0.1:8000/metrics

Metrics include: request count and API latency

📝 Logging
Application logs are stored in: logs/app.log

Logs include:
user queries
response generation
backend activity

🔥 Example Query
How do I reset my password?
Example Response : Go to Settings > Account > Reset Password. Enter your email and click Send OTP.

🧠 Key Concepts Implemented
Retrieval-Augmented Generation (RAG)
Semantic Search
Vector Databases
Embeddings
Workflow Orchestration
REST APIs
Monitoring & Observability
AI Application Architecture

🚀 Future Improvements
Dockerization
Cloud deployment
Conversation memory
Multi-document support
Authentication
Real human escalation workflow
Advanced RAG optimization

👨‍💻 Author
Amulya

📜 License
This project is developed for learning and educational purposes.
