# app.py
import streamlit as st
from langchain_core.messages import HumanMessage
from agent.implementation_graph import agent as implementation_agent
from agent.qa_agent import agent as qa_agent
import uuid

st.set_page_config(page_title="Shopify Dev Assistant", page_icon="🛍️")
st.title("Shopify Theme Dev Assistant")

# --- Session state init ---
if "stage" not in st.session_state:
    st.session_state.stage = "input"          # input → implementing → review → qa_running → done
if "feature_request" not in st.session_state:
    st.session_state.feature_request = None
if "implementation" not in st.session_state:
    st.session_state.implementation = None
if "qa_report" not in st.session_state:
    st.session_state.qa_report = None

# --- Stage: input ---
if st.session_state.stage == "input":
    feature_request = st.text_area("Describe the feature you want to build:")
    if st.button("Generate implementation") and feature_request:
        st.session_state.feature_request = feature_request
        st.session_state.stage = "implementing"
        st.rerun()

# --- Stage: implementing ---
if st.session_state.stage == "implementing":
    with st.spinner("Generating implementation..."):
        result = implementation_agent.invoke(
            {"messages": [HumanMessage(content=st.session_state.feature_request)]},
            config={"configurable": {"thread_id": str(uuid.uuid4())}}
        )
        st.session_state.implementation = result["messages"][-1].content
        st.session_state.stage = "review"
        st.rerun()

# --- Stage: review (human gate) ---
if st.session_state.stage == "review":
    st.markdown("### Implementation")
    st.markdown(st.session_state.implementation)
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        if st.button("✅ Send to QA", type="primary"):
            st.session_state.stage = "qa_running"
            st.rerun()
    with col2:
        if st.button("🔄 Start over"):
            for key in ["stage", "feature_request", "implementation", "qa_report"]:
                del st.session_state[key]
            st.rerun()

# --- Stage: QA running ---
if st.session_state.stage == "qa_running":
    with st.spinner("Running QA review..."):
        qa_result = qa_agent.invoke(
            {"messages": [HumanMessage(content=f"""
Feature request: {st.session_state.feature_request}

Implementation to review:
{st.session_state.implementation}
""")]},
            config={"configurable": {"thread_id": str(uuid.uuid4())}}
        )
        st.session_state.qa_report = qa_result["messages"][-1].content
        st.session_state.stage = "done"
        st.rerun()

# --- Stage: done ---
if st.session_state.stage == "done":
    st.markdown("### Implementation")
    st.markdown(st.session_state.implementation)
    st.divider()
    st.markdown("### QA Report")
    st.markdown(st.session_state.qa_report)
    if st.button("🔄 Start over"):
        for key in ["stage", "feature_request", "implementation", "qa_report"]:
            del st.session_state[key]
        st.rerun()