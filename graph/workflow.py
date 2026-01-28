from langgraph.graph import StateGraph, END

from agents.collector import collector_agent
from agents.extractor import extractor_agent
from agents.impact import impact_agent
from agents.writer import writer_agent


def build_graph(mcp):
    graph = StateGraph(dict)

    graph.add_node("collector", lambda state: collector_agent(state, mcp))
    graph.add_node("extractor", lambda state: extractor_agent(state, mcp))
    graph.add_node("impact", lambda state: impact_agent(state, mcp))
    graph.add_node("writer", lambda state: writer_agent(state, mcp))

    graph.set_entry_point("collector")

    graph.add_edge("collector", "extractor")
    graph.add_edge("extractor", "impact")
    graph.add_edge("impact", "writer")

    # 🔴 THIS LINE FIXES THE ERROR
    graph.add_edge("writer", END)

    return graph.compile()
