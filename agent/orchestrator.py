from langgraph.checkpoint.memory import MemorySaver
from langchain_core.messages import HumanMessage
from agent.implementation_graph import agent as implementation_agent
from agent.qa_agent import agent as qa_agent
import uuid


# feature_request = input("Enter a feature request: ")
# Step 1 — run implementation agent
feature_request = input("Enter a feature request: ")
# Step 1 — implementation agent
impl_result = implementation_agent.invoke(
    {"messages": [HumanMessage(content=feature_request)]},
    config={"configurable": {"thread_id": str(uuid.uuid4())}}
)
implementation = impl_result["messages"][-1].content
print("\n=== IMPLEMENTATION ===")
print(implementation)

# Step 2 — human gate
approved = input("\nSend to QA agent? (y/n): ")
if approved.lower() != "y":
    print("QA review cancelled.")
    exit()

# Step 3 — QA agent runs to completion in one invoke
qa_result = qa_agent.invoke(
    {"messages": [HumanMessage(content=f"""
Feature request: {feature_request}

Implementation to review:
{implementation}
""")]},
    config={"configurable": {"thread_id": str(uuid.uuid4())}}
)
print("\n=== QA REPORT ===")
print(qa_result["messages"][-1].content)