# import pprint
# # for event in agent.stream({"messages": [{"role": "user", "content": "How do I break out of a for loop early in Liquid?"}]}, config=config, stream_mode = "updates"):
# #      pprint.pp(event) 

# # for event in agent.stream({"messages": [{"role": "user", "content": "What's the difference between assign and capture in Liquid?"}]}, config=config, stream_mode = "updates"):
# #      pprint.pp(event)

    
# # for event in agent.stream({"messages": [{"role": "user", "content": "How do I write a comment in Liquid that won't appear in the output?"}]}, config=config, stream_mode = "updates"):
# #      pprint.pp(event)

# # for event in agent.stream({"messages": [{"role": "user", "content": "How do I paginate results in Liquid?"}]}, config=config, stream_mode = "updates"):
# #     pprint.pp(event)

# test_queries = [
#     # Tags
#     "How do I create a variable in Liquid?",
#     "How do I break out of a for loop early in Liquid?",
#     "What's the difference between assign and capture in Liquid?",
#     "How do I write a comment in Liquid that won't appear in the output?",
#     "How do I paginate results in Liquid?",
#     # Filters
#     "How do I convert a string to uppercase in Liquid?",
#     "How do I round a number to 2 decimal places in Liquid?",
#     "How do I display a product price with currency in Liquid?",
#     "How do I remove duplicate items from an array in Liquid?",
#     "How do I sort a collection of products by price?",
#     # Objects
#     "How do I access a product's title and price in Liquid?",
#     "How do I get the current customer's email address in Liquid?",
#     "How do I access metafields on a product object?",
#     "How do I get the URL of a product's featured image?",
#     # Trap question
#     "What's the difference between a section and a snippet in Shopify themes?",
# ]

# for i, query in enumerate(test_queries, 1):
#     print(f"\n{'='*60}")
#     print(f"Q{i}: {query}")
#     print('='*60)
#     result = agent.invoke({"messages": [{"role": "user", "content": query}]})
#     final = result["messages"][-1].content
#     print(f"A: {final}")

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

SYSTEM_PROMPT = """You are a Shopify Liquid documentation assistant.
You MUST use the search_shopify_docs tool to answer every question.
If the first search doesn't return relevant results, try rephrasing the query and search again.
Only after two attempts should you say: "I couldn't find that in the Shopify docs."
ONLY answer based on what the tool returns.
NEVER answer from your own knowledge about Liquid or Shopify."""

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


test_queries = [
    # Tags
    "How do I create a variable in Liquid?",
    "How do I break out of a for loop early in Liquid?",
    "What's the difference between assign and capture in Liquid?",
    "How do I write a comment in Liquid that won't appear in the output?",
    "How do I paginate results in Liquid?",
    # Filters
    "How do I convert a string to uppercase in Liquid?",
    "How do I round a number to 2 decimal places in Liquid?",
    "How do I display a product price with currency in Liquid?",
    "How do I remove duplicate items from an array in Liquid?",
    "How do I sort a collection of products by price?",
    # Objects
    "How do I access a product's title and price in Liquid?",
    "How do I get the current customer's email address in Liquid?",
    "How do I access metafields on a product object?",
    "How do I get the URL of a product's featured image?",
    # Trap question
    "What's the difference between a section and a snippet in Shopify themes?",
]

for i, query in enumerate(test_queries, 1):
    print(f"\n{'='*60}")
    print(f"Q{i}: {query}")
    print('='*60)
    result = agent.invoke({"messages": [{"role": "user", "content": query}]})
    final = result["messages"][-1].content
    print(f"A: {final}")