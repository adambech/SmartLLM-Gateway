from fastapi import FastAPI

app = FastAPI(
    title="SmartLLM Gateway",
    description="A cost-aware LLM gateway with semantic caching and intelligent routing.",
    version="0.1.0",
)


@app.get("/api/v1/health")
async def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "service": "smartllm-gateway",
    }
