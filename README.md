# Market Research & Impact Analysis Framework  
(Agentic AI + Model Context Protocol)

## 1. Overview

This project implements a Backend Framework for automated market research using an Agentic AI architecture.  
Multiple AI agents collaborate in a linear pipeline to generate a structured Market Intelligence Report for industry 

A key requirement of this assignment is the strict decoupling of AI logic from execution tools using the Model Context Protocol (MCP).  
Agents do not execute Python functions directly and interact with the external world only through MCP tools.

---

## 2. System Architecture

### 2.1 Agentic Workflow (The “Brain”)

The system orchestrates four agents in sequence using LangGraph:

1. Collector Agent  
   - Identifies relevant news, regulatory updates, and external signals  
   - Calls MCP tools for web search  

2. Extractor Agent  
   - Fetches raw content  
   - Cleans and extracts structured entities (competitors, themes)  

3. Impact Agent  
   - Analyzes extracted data  
   - Assigns impact level (High / Medium / Low)  
   - Generates impact score, reasoning, and actionable recommendations  

4. Report Writer Agent  
   - Aggregates all insights  
   - Produces the final report strictly adhering to the required JSON schema  

---

### 2.2 MCP Server (The “Hands”)

All external actions are exposed via an MCP Server.  
Agents interact with the outside world only through these tools:

- search_web(query)  
- fetch_url(url)  
- clean_extract(raw_text)  
- extract_entities(text)  
- dedupe_items(list)  
- impact_score(item, context)  
- generate_market_report(data)  

The MCP server handles failures gracefully (e.g., invalid URLs) so the pipeline never crashes.

---

## 3. Tech Stack (Open Source Only)

- Language: Python 3.10+  
- LLM Inference: Ollama (Llama3 / Mistral / Qwen2.5)  
- Orchestration: LangGraph  
- API Framework: FastAPI  
- Scraping: Trafilatura  

Note: No paid APIs (OpenAI, Anthropic, Serper, etc.) are used.

---

## 4. API Specification

### 4.1 POST /analyze

Triggers the full agentic research pipeline.

Request:
```
{
"industry": "NBFC",
"from": "2026-01-01",
"to": "2026-01-15",
"focus": "regulatory"
}
```
Response :
Response:
```json
{
  "report_id": "report_001",
  "report": {
    "summary": "High-level executive summary...",
    "drivers": ["Driver 1", "Driver 2"],
    "competitors": ["Comp A", "Comp B", "Comp C", "Comp D", "Comp E"],
    "impact_radar": [
      {
        "event": "RBI releases new guidelines",
        "impact_level": "High",
        "score": 85,
        "why": ["Direct compliance cost", "Requires process change"],
        "actions": ["Audit current flows", "Update legal policy"],
        "url": "https://..."
      }
    ],
    "opportunities": ["Opp 1...", "Opp 2..."],
    "risks": ["Risk 1...", "Risk 2..."],
    "90_day_plan": {
      "0_30": ["Immediate action 1..."],
      "30_60": ["Mid-term strategy..."],
      "60_90": ["Long-term optimization..."]
    },
    "sources": ["url1", "url2"]
  }
}
```
5. Running the Project Locally

Install dependencies:
```pip install -r requirements.txt```

Start Ollama:
```ollama serve```

Start MCP Server:
```uvicorn mcp_server.server:app --port 8001```

Start API Server:
```uvicorn api.main:app --port 8000```



