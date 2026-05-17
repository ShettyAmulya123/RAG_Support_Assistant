from prometheus_client import Counter, Histogram


# Total API requests
REQUEST_COUNT = Counter(
    "rag_requests_total",
    "Total number of RAG requests"
)

# API latency
REQUEST_LATENCY = Histogram(
    "rag_request_latency_seconds",
    "RAG API latency"
)