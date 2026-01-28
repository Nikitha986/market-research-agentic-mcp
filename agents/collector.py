def collector_agent(state, mcp):
    print("[Collector] calling MCP tool: search_web")
    res = mcp("search_web", {"query": state["industry"]})

    return {
        **state,
        "sources": res["results"]
    }
