import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, MessagesState, END
from langgraph.prebuilt import ToolNode
from agent.tools import tools
from langgraph.checkpoint.memory import MemorySaver

llm = ChatOpenAI(model="gpt-4o")
tools = [tools.search_shopify_docs]
llm_with_tools = llm.bind_tools(tools)

SYSTEM_PROMPT = """You are a Shopify Liquid code quality agent. You review implementations produced by another agent and check them against the official Shopify documentation.

You MUST use search_shopify_docs for EVERY piece of Liquid syntax in the implementation — every tag, filter, and object property — before issuing any verdict. Do not rely on your own knowledge.

For each implementation you receive, produce a structured QA report with three sections:

## 1. Syntax check
For every Liquid tag, filter, and object property used:
- Search the docs to confirm it exists and is used correctly
- Flag anything you cannot verify with: UNVERIFIED: [syntax] — could not confirm in docs
- Flag anything used incorrectly with: INCORRECT: [syntax] — docs say [correct usage]

## 2. Completeness check
- Restate the original feature request
- List every requirement it implies
- Mark each as MET or UNMET with a one-line explanation

## 3. Best practices check
Search the docs for guidance on:
- Edge cases the implementation doesn't handle (e.g. product with no images, customer not logged in, empty collection)
- Shopify-specific conventions the implementation violates or misses
- Security or performance concerns documented by Shopify

## Final verdict
PASS — implementation is correct, complete, and follows documented best practices
FAIL — one or more issues found. List each with severity: CRITICAL / WARNING / SUGGESTION

CRITICAL: incorrect syntax or missing required functionality
WARNING: unverified syntax or unhandled edge case
SUGGESTION: best practice improvement with no functional impact

Never issue a PASS if any syntax is UNVERIFIED. A PASS means every piece of syntax has been confirmed against the docs."""

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

agent = graph.compile(
    checkpointer=MemorySaver()
)

# test_query = """ 
# Implementation to review:
# Based on the verified Shopify documentation, here is how you can display the current product's title, price, and vendor on a product page using Shopify Liquid:

# ```liquid
# <h1>{{ product.title }}</h1>
# <p>Price: {{ product.price | money }}</p>
# <p>Vendor: {{ product.vendor }}</p>
# ```

# ### Explanation:
# - `{{ product.title }}`: This Liquid tag fetches and displays the title of the current product. This information was verified from the [product Liquid object documentation](https://shopify.dev/docs/api/liquid/objects/product).

# - `{{ product.price | money }}`: This fetches the price of the current product and formats it using the `money` filter. The usage of `product.price` and the `money` filter was verified from the [product Liquid object documentation](https://shopify.dev/docs/api/liquid/filters/money-filters).
#   - Note: Depending on the product's pricing and currency setup, you might need to adjust this further (e.g., for multiple variants).

# - `{{ product.vendor }}`: This fetches and displays the vendor of the current product. This usage was confirmed in the [product and vendor documentation](https://shopify.dev/docs/api/liquid/objects/product).

# This code can be added to your product template file in your Shopify theme to display the respective details on the product page.

# """

# result = agent.invoke({"messages": [{"role": "user", "content": test_query}]})
# final = result["messages"][-1].content
# print(f"A: {final}")