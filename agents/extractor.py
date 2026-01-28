def extractor_agent(state, mcp):
    extracted = []

    for src in state["sources"]:
        print("[Extractor] calling MCP tool: fetch_url")
        raw = mcp("fetch_url", {"url": src["url"]})

        print("[Extractor] calling MCP tool: clean_extract")
        clean = mcp("clean_extract", {
            "raw_text": raw["raw_text"]
        })

        print("[Extractor] calling MCP tool: extract_entities")
        entities = mcp("extract_entities", {
            "text": clean["clean_text"]
        })

        extracted.append({
            "entities": entities,
            "url": src["url"]
        })

    return {
        **state,
        "extracted": extracted
    }
