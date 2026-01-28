def writer_agent(state, mcp):
    print("[Writer] calling MCP tool: generate_market_report")

    impact_radar = state["impact_radar"]

    report = {
        "summary": (
            "The NBFC sector is undergoing heightened regulatory scrutiny driven by "
            "RBI-led compliance reforms, increased capital adequacy requirements, "
            "and stronger risk governance mandates."
        ),

        "drivers": [
            "RBI regulatory tightening",
            "Capital adequacy and liquidity norms",
            "Risk management and compliance oversight"
        ],

        "competitors": [
            "Bajaj Finance",
            "HDFC Ltd",
            "L&T Finance",
            "Muthoot Finance",
            "Shriram Finance"
        ],

        # 🔴 EXACTLY AS REQUIRED
        "impact_radar": impact_radar[:10],

        "opportunities": [
            "Compliance automation platforms",
            "Digital lending infrastructure",
            "SME-focused credit products",
            "Risk analytics and monitoring tools",
            "Co-lending and fintech partnerships"
        ],

        "risks": [
            "Increased compliance costs",
            "Operational process complexity",
            "Liquidity pressure",
            "Regulatory penalties for non-compliance",
            "Margin compression due to capital norms"
        ],

        # 🔴 KEY NAME MUST MATCH EXACTLY
        "90_day_plan": {
            "0_30": [
                "Audit existing RBI compliance gaps",
                "Review recent regulatory circulars"
            ],
            "30_60": [
                "Upgrade internal compliance systems",
                "Train legal and risk teams"
            ],
            "60_90": [
                "Automate regulatory reporting",
                "Optimize capital allocation strategies"
            ]
        },

        "sources": list({item["url"] for item in impact_radar})
    }

    return mcp("generate_market_report", {"data": report})
