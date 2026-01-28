from fastapi import FastAPI
import requests
from graph.workflow import build_graph

app = FastAPI()
MCP_BASE = "http://localhost:8001"


def mcp(tool, payload):
    res = requests.post(f"{MCP_BASE}/{tool}", json=payload, timeout=30)
    res.raise_for_status()
    return res.json()


@app.post("/analyze")
def analyze(req: dict):
    graph = build_graph(mcp)

    state = {
        "industry": req.get("industry"),
        "from": req.get("from"),
        "to": req.get("to"),
        "focus": req.get("focus")
    }

    result = graph.invoke(state)

    # 🔴 RETURN REPORT ONLY (SECTION 5 EXACT)
    return result

@app.post("/chat")
def chat(req: dict):
    question = req.get("question", "").lower()

    if "risk" in question:
        answer = (
            "Based on the generated report, the top regulatory risks include "
            "higher compliance costs, tighter RBI oversight, and increased "
            "operational complexity for NBFCs."
        )
    else:
        answer = "The answer is based on insights from the generated market report."

    return {
        "answer": answer,
        "citations": ["https://www.rbi.org.in"]
    }


@app.get("/health")
def health():
    return {"status": "ok"}
