from fastapi import FastAPI
from mcp_server.tools import (
    search_web,
    fetch_url,
    clean_extract,
    extract_entities,
    dedupe_items,
    impact_score,
    generate_market_report
)

app = FastAPI()


@app.post("/search_web")
def tool_search(payload: dict):
    return search_web(payload["query"])


@app.post("/fetch_url")
def tool_fetch(payload: dict):
    return fetch_url(payload["url"])


@app.post("/clean_extract")
def tool_clean(payload: dict):
    return clean_extract(payload["raw_text"])


@app.post("/extract_entities")
def tool_extract(payload: dict):
    text = payload.get("text", "")
    return extract_entities(text)



@app.post("/dedupe_items")
def tool_dedupe(payload: dict):
    return dedupe_items(payload["items"])


@app.post("/impact_score")
def tool_impact(payload: dict):
    return impact_score(payload["item"], payload["context"])


@app.post("/generate_market_report")
def tool_report(payload: dict):
    return generate_market_report(payload["data"])
