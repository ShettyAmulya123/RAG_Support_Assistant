from fastapi import FastAPI
from pydantic import BaseModel

from app.rag.graph import app as rag_workflow

from app.logging_config import logger

import time

from prometheus_client import generate_latest
from fastapi.responses import Response

from app.metrics import (
    REQUEST_COUNT,
    REQUEST_LATENCY
)


# Create FastAPI app
api = FastAPI()


# Request schema
class QueryRequest(BaseModel):
    query: str


# Root endpoint
@api.get("/")
def home():
    return {
        "message": "RAG Support Assistant API Running"
    }


# Chat endpoint
@api.post("/chat")
def chat(request: QueryRequest):

    logger.info(f"Received query: {request.query}")

    start_time = time.time()

    result = rag_workflow.invoke({
        "query": request.query
    })

    REQUEST_COUNT.inc()

    REQUEST_LATENCY.observe(
        time.time() - start_time
    )

    logger.info("Response generated successfully")

    return {
        "query": request.query,
        "answer": result["answer"]
    }
    
# Metrics Endpoint
@api.get("/metrics")
def metrics():
    return Response(
        generate_latest(),
        media_type="text/plain"
    )    