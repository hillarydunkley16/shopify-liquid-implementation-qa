import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, MessagesState, END
from langgraph.prebuilt import ToolNode
from agent.tools import tools


llm = ChatOpenAI(model="gpt-4o")
tools = [tools.search_shopify_docs]
llm_with_tools = llm.bind_tools(tools)

SYSTEM_PROMPT = """You are a Shopify theme implementation agent.

Given a feature request, you MUST:
1. Call search_shopify_docs to find relevant Liquid syntax before writing any code
2. Always generate a complete implementation — never refuse
3. For syntax confirmed by the tool, cite the source URL
4. For syntax you could not confirm, include it but flag it inline with a comment:
   {%- comment -%} UNVERIFIED: could not confirm this in docs {%- endcomment -%}

Return a complete, copy-pasteable implementation with a brief explanation of each part."""
def call_model(state):
    messages = [SystemMessage(content=SYSTEM_PROMPT)] + state["messages"]
    response = llm_with_tools.invoke(messages)
    return {"messages": [response]}

def should_continue(state):
    last = state["messages"][-1]
    return "tools" if last.tool_calls else END

tool_node = ToolNode(tools)

graph = StateGraph(MessagesState)
graph.add_node("model", call_model)
graph.add_node("tools", tool_node)
graph.set_entry_point("model")
graph.add_conditional_edges("model", should_continue)
graph.add_edge("tools", "model")

agent = graph.compile()
