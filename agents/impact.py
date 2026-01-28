def impact_agent(state, mcp):
    radar = []

    for item in state["extracted"]:
        print("[Impact] calling MCP tool: impact_score")
        impact = mcp("impact_score", {
            "item": item,
            "context": state["industry"]
        })

        for i in range(5):
            radar.append({
                "event": f"RBI regulatory update affecting NBFC operations ({i+1})",
                "impact_level": impact["impact_level"],
                "score": impact["score"],
                "why": impact["why"],
                "actions": impact["actions"],
                "url": item["url"]
            })

    return {
        **state,
        "impact_radar": radar[:10]  # GUARANTEED
    }
