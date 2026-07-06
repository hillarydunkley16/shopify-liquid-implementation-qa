import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from agent.graph import agent
import uuid
st.set_page_config(page_title="Shopify Liquid Docs Assistant", page_icon=":robot_face:")
st.title("Shopify Liquid Docs Assistant")
st.write("Ask questions about Shopify's Liquid templating language and get answers based on the official documentation.")

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())
if "messages" not in st.session_state:
    st.session_state.messages = []
config = {"configurable": {"thread_id": st.session_state.thread_id}}


# --- Render existing conversation ---
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- Sidebar: new conversation button ---
with st.sidebar:
    st.markdown("### Session")
    st.caption(f"Thread: `{st.session_state.thread_id[:8]}...`")
    if st.button("Start new conversation"):
        st.session_state.thread_id = str(uuid.uuid4())
        st.session_state.messages = []
        st.rerun()

# --- Chat input ---
user_input = st.chat_input("Ask a question about Shopify Liquid...")

if user_input:
    # Show the user's message immediately
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Run the agent
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            final_response = None
            tool_calls_made = []

            for event in agent.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=config,
                stream_mode="updates",
            ):
                print("Event:", event)
                # Track tool calls for an optional "what it checked" expander
                if "tools" in event:
                    for m in event["tools"]["messages"]:
                        tool_calls_made.append(m.name)
                        print(f"Tool called: {m.name}")
                if "model" in event:
                    last_msg = event["model"]["messages"][-1]
                    print("Agent message:", last_msg)
                    if isinstance(last_msg, AIMessage) and last_msg.content:
                        print("Streaming response:", last_msg.content)
                        final_response = last_msg.content

            if tool_calls_made:
                with st.expander(f"Checked: {', '.join(tool_calls_made)}"):
                    st.caption("Tools called while answering this question.")

            response_text = final_response or "I wasn't able to find an answer to that."
            st.markdown(response_text)

    st.session_state.messages.append({"role": "assistant", "content": response_text})