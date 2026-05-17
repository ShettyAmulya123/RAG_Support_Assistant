from typing import TypedDict

from langgraph.graph import StateGraph, END

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

from app.rag.llm import generate_answer


# -----------------------------
# STATE DEFINITION
# -----------------------------
class GraphState(TypedDict):
    query: str
    context: str
    answer: str
    score: float


# -----------------------------
# LOAD VECTOR DATABASE
# -----------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.load_local(
    "vectorstore",
    embedding_model,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)


# -----------------------------
# NODE 1 — RETRIEVAL
# -----------------------------
def retrieve_node(state: GraphState):

    print("\n--- RETRIEVING CONTEXT ---\n")

    query = state["query"]

    results = vectorstore.similarity_search_with_score(
        query,
        k=3
    )

    docs = []
    scores = []

    for doc, score in results:
        docs.append(doc)
        scores.append(score)

    context = "\n".join([
        doc.page_content for doc in docs
    ])

    best_score = min(scores) if scores else 999

    print(f"Best similarity score: {best_score}")

    return {
        "query": query,
        "context": context,
        "score": best_score
    }


# -----------------------------
# NODE 2 — ANSWER GENERATION
# -----------------------------
def answer_node(state: GraphState):

    print("\n--- GENERATING ANSWER ---\n")

    query = state["query"]
    context = state["context"]

    answer = generate_answer(query, context)

    return {
        "query": query,
        "context": context,
        "answer": answer
    }


# -----------------------------
# NODE 3 — ESCALATION
# -----------------------------
def escalate_node(state: GraphState):

    print("\n--- ESCALATING TO HUMAN ---\n")

    return {
        "query": state["query"],
        "context": state["context"],
        "answer": "Your query has been escalated to a human support agent."
    }


# -----------------------------
# CONDITIONAL ROUTING
# -----------------------------
def route_decision(state: GraphState):

    score = state["score"]

    print(f"\nRouting score: {score}\n")

    if score > 1.0:
        return "escalate"

    return "answer"


# -----------------------------
# BUILD GRAPH
# -----------------------------
workflow = StateGraph(GraphState)

# Add nodes
workflow.add_node("retrieve", retrieve_node)
workflow.add_node("answer", answer_node)
workflow.add_node("escalate", escalate_node)

# Entry point
workflow.set_entry_point("retrieve")

# Conditional edges
workflow.add_conditional_edges(
    "retrieve",
    route_decision,
    {
        "answer": "answer",
        "escalate": "escalate"
    }
)

# Ending edges
workflow.add_edge("answer", END)
workflow.add_edge("escalate", END)

# Compile graph
app = workflow.compile()


# -----------------------------
# RUN WORKFLOW
# -----------------------------
query = input("Ask your question: ")

result = app.invoke({
    "query": query
})

print("\nFINAL RESPONSE:\n")
print(result["answer"])