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

# SYSTEM_PROMPT = """You are a Shopify theme implementation agent.

# Given a feature request, you MUST:
# 1. Call search_shopify_docs to find relevant Liquid syntax, objects, and filters before writing any code
# 2. Base your implementation ONLY on what the tool returns — never invent syntax
# 3. Return a complete, copy-pasteable implementation with:
#    - The Liquid template code
#    - Any required JavaScript
#    - A brief explanation of what each part does and which Shopify doc it came from

# If search_shopify_docs does not return relevant results for a required piece of syntax,
# say explicitly: "I could not verify [X] in the docs — treat this part as unconfirmed."

# NEVER write Liquid syntax you haven't confirmed through the tool.
# "If search_shopify_docs returns results that are not directly relevant to the request, "
# "do NOT generate code. Say: 'I couldn't find verified documentation for this feature. "
# "I won't generate unconfirmed code as it could break your store.'"
# """

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

# test_queries = [
#     # Basic object access
#     "Display the current product's title, price, and vendor on a product page",
#     "Show the number of items in the cart and the cart's total price",
#     "Display the current customer's name and email if they are logged in",
#     # Filters
#     "Display a product price formatted with currency symbol and two decimal places",
#     "Truncate a product description to 100 words with an ellipsis",
#     "Convert a product handle to a readable title with proper capitalization",
#     # Control flow
#     "Loop through all products in a collection and display only those that are in stock",
#     "Display a sale badge on a product if its price is lower than its compare-at price",
#     "Show a different message depending on whether the customer is logged in or not",
#     # Pagination and collections
#     "Paginate a collection of products showing 12 per page with navigation links",
#     "Build a sort dropdown for a collection page that lets users sort by price or best-selling",
#     # Harder / multi-concept
#     "Display all images in a product's media gallery as clickable thumbnails",
#     "Show a product's metafield value for a custom field called 'material' under the 'details' namespace",
#     "Build a size guide that only displays if a product is tagged with 'has-size-guide'",
#     # Trap question
#     "Build a custom checkout page that collects additional customer information",
# ]

# for i, query in enumerate(test_queries, 1):
#     print(f"\n{'='*60}")
#     print(f"Q{i}: {query}")
#     print('='*60)
#     result = agent.invoke({"messages": [{"role": "user", "content": query}]})
#     final = result["messages"][-1].content
#     print(f"A: {final}")

