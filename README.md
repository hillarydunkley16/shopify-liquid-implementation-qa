# Shopify Liquid Implementation & QA

An LLM-powered assistant for generating and reviewing Shopify Liquid theme implementations using retrieval-augmented generation (RAG) over Shopify's official Liquid documentation.

The project combines **LlamaIndex**, **LangChain**, **LangGraph**, **OpenAI**, and **Streamlit** to provide two related workflows:

1. **Liquid Documentation Assistant** — answers questions about Shopify Liquid using a searchable index of Shopify documentation.
2. **Implementation & QA Assistant** — takes a Shopify theme feature request, generates an implementation grounded in the documentation, and sends it through an independent QA agent for syntax, completeness, and best-practice review.

## Overview

Shopify Liquid is a templating language used to build dynamic Shopify themes. Writing Liquid correctly requires knowing the syntax and behavior of Shopify-specific objects, tags, and filters.

This project explores whether LLM agents can make Shopify theme development more reliable by requiring the model to retrieve relevant documentation before generating or evaluating Liquid code.

The core design principle is:

> **Retrieve first, generate second, verify independently.**

Rather than relying entirely on an LLM's pretrained knowledge of Liquid, the agents use a RAG pipeline containing Shopify documentation. The implementation agent uses that documentation to inform generated code, while a separate QA agent independently checks the resulting implementation against the same documentation.

## Architecture

```text
                         Shopify Liquid Docs
                                │
                                ▼
                    ┌───────────────────────┐
                    │   Ingestion Pipeline  │
                    │                       │
                    │ Markdown documents    │
                    │ Sentence splitting    │
                    │ OpenAI embeddings     │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │   LlamaIndex Index    │
                    │                       │
                    │ Vector store          │
                    │ Document metadata     │
                    └───────────┬───────────┘
                                │
                         search_shopify_docs
                                │
              ┌─────────────────┴──────────────────┐
              │                                    │
              ▼                                    ▼
     Documentation Agent                   Implementation Agent
              │                                    │
              │                                    ▼
              │                            Generated Liquid
              │                                    │
              │                             Human Review
              │                                    │
              │                                    ▼
              │                              QA Agent
              │                                    │
              │                                    ▼
              │                              QA Report
              │
              ▼
       Streamlit Chat UI
```

The implementation and QA agents are built as LangGraph state graphs. Each graph alternates between the language model and a tool node that performs documentation retrieval.

## Features

### Documentation-grounded Liquid assistance

The documentation assistant is instructed to use the `search_shopify_docs` tool for every question and to base its answer only on retrieved documentation. If the initial search is insufficient, it can rephrase the query and search again before reporting that the documentation could not be found.

Example questions include:

* How do I create a variable in Liquid?
* How do I break out of a `for` loop?
* What's the difference between `assign` and `capture`?
* How do I paginate a collection?
* How do I access product metafields?
* How do I format a product price?

### Documentation-grounded implementation

The implementation agent accepts a natural-language feature request and generates a complete Shopify theme implementation.

The agent is instructed to:

1. Search the Shopify documentation before generating Liquid.
2. Use retrieved documentation as the basis for its implementation.
3. Provide copy-pasteable Liquid code.
4. Include JavaScript when required.
5. Cite documentation for confirmed syntax.
6. Flag syntax that could not be verified.

Example feature requests include:

* Display product title, price, and vendor.
* Show the number of items in the cart and the cart total.
* Display a customer's name and email when logged in.
* Filter products based on inventory status.
* Display a sale badge based on compare-at pricing.
* Paginate a collection.
* Display product media thumbnails.
* Display a product metafield.
* Conditionally display a size guide.

### Independent QA review

The QA agent reviews an implementation produced by the implementation agent rather than simply accepting the generated output.

It performs three categories of checks:

#### 1. Syntax check

Every Liquid tag, filter, and object property is checked against the documentation retrieval tool.

The QA agent can classify findings as:

* `INCORRECT` — the documentation contradicts the implementation.
* `UNVERIFIED` — the syntax could not be confirmed.
* Verified — the retrieved documentation supports the usage.

#### 2. Completeness check

The agent decomposes the original feature request into individual requirements and marks each as:

* `MET`
* `UNMET`

#### 3. Best-practices check

The agent searches for relevant Shopify guidance concerning:

* Edge cases
* Shopify-specific conventions
* Security
* Performance

The final verdict is:

* **PASS** — all required syntax is verified and the implementation is correct and complete.
* **FAIL** — one or more issues are identified.

Issues are categorized as:

* **CRITICAL** — incorrect syntax or missing required functionality
* **WARNING** — unverified syntax or an unhandled edge case
* **SUGGESTION** — a best-practice improvement without functional impact

The QA agent is explicitly instructed not to issue a PASS when any syntax remains unverified.

## RAG Pipeline

The documentation corpus is processed using LlamaIndex.

The ingestion pipeline:

1. Loads Markdown files recursively from `docs/`.
2. Classifies documents based on their paths.
3. Splits documents into chunks.
4. Generates embeddings using OpenAI's `text-embedding-3-small`.
5. Persists the ingestion pipeline and vector index locally.

Documents are classified into:

* `liquid_filter`
* `liquid_object`
* `liquid_tag`
* `theme_doc`

The resulting index is stored under `scripts/storage/`.

The retrieval tool loads this persisted index and returns the top three relevant source chunks, including their filename, document type, similarity score, and text.

## Project Structure

```text
shopify-liquid-implementation-qa/
│
├── agent/
│   ├── tools/
│   │   └── tools.py
│   │
│   ├── agent.py
│   ├── graph.py
│   ├── implementation_graph.py
│   ├── orchestrator.py
│   └── qa_agent.py
│
├── docs/
│   └── api/
│       └── ...
│
├── scripts/
│   ├── ingestion.py
│   ├── query.py
│   ├── pipeline_cache/
│   └── storage/
│
├── app.py
├── streamlit_app.py
├── requirements.txt
├── test_questions_coding.txt
└── test_questions_qanda.txt
```

The repository currently contains two Streamlit entry points:

* `streamlit_app.py` — documentation Q&A interface.
* `app.py` — implementation generation and QA workflow.

### `agent/`

Contains the LangGraph-based agents.

* `agent.py` — documentation Q&A agent.
* `graph.py` — theme implementation agent.
* `implementation_graph.py` — implementation-generation workflow used by the main application.
* `qa_agent.py` — independent implementation reviewer.
* `orchestrator.py` — command-line implementation → human approval → QA workflow.
* `tools/tools.py` — documentation retrieval tool.

### `scripts/`

Contains the document ingestion and retrieval setup.

* `ingestion.py` builds the vector index.
* `query.py` provides a standalone retrieval/query experiment.
* `storage/` contains the persisted LlamaIndex index.
* `pipeline_cache/` contains persisted ingestion data.

### `docs/`

Contains the Shopify documentation corpus used for retrieval. Documents are organized into categories such as filters, objects, tags, and other theme documentation.

### `app.py`

Provides the end-to-end Streamlit workflow:

```text
Feature request
      ↓
Implementation Agent
      ↓
Human review
      ↓
QA Agent
      ↓
QA Report
```

The human review step is intentional: the generated implementation is displayed before the user decides whether to send it to QA.

### `streamlit_app.py`

Provides a conversational interface for asking questions about Shopify Liquid. It maintains a conversation thread and displays which retrieval tools were called while answering a question.

## Tech Stack

| Technology                   | Purpose                                     |
| ---------------------------- | ------------------------------------------- |
| Python                       | Application and agent logic                 |
| Streamlit                    | User interface                              |
| LangGraph                    | Agent orchestration and tool-calling graphs |
| LangChain                    | LLM/tool integration                        |
| OpenAI                       | LLM inference and embeddings                |
| LlamaIndex                   | Document ingestion, indexing, and retrieval |
| Shopify Liquid documentation | Grounding corpus                            |

The current dependency list includes Streamlit, LangChain Core/OpenAI, LangGraph, and LlamaIndex.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/hillarydunkley16/shopify-liquid-implementation-qa.git
cd shopify-liquid-implementation-qa
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the OpenAI API key

The retrieval tool expects an OpenAI API key through Streamlit secrets.

Create:

```text
.streamlit/secrets.toml
```

with:

```toml
OPENAI_API_KEY = "your-api-key"
```

Do not commit this file or expose the API key publicly.

## Build the Documentation Index

If the persisted index is not already available, run the ingestion pipeline:

```bash
cd scripts
python ingestion.py
```

The ingestion process reads Markdown documentation from `docs/`, generates embeddings, and writes the resulting index to `scripts/storage/`.

Then return to the project root:

```bash
cd ..
```

## Run the Applications

### Documentation Assistant

Run:

```bash
streamlit run streamlit_app.py
```

This launches the conversational Liquid documentation assistant.

### Implementation + QA Assistant

Run:

```bash
streamlit run app.py
```

The application follows this workflow:

```text
1. Enter feature request
2. Generate implementation
3. Review generated implementation
4. Send implementation to QA
5. Review QA report
```

The implementation is not automatically sent to QA; the application includes an explicit human approval step.

## Command-Line Workflow

The same implementation → human review → QA sequence can be run without Streamlit:

```bash
python -m agent.orchestrator
```

The orchestrator:

1. Prompts for a feature request.
2. Runs the implementation agent.
3. Displays the generated implementation.
4. Asks whether it should be sent to QA.
5. Runs the QA agent if approved.
6. Prints the resulting QA report.

## Design Decisions

### Retrieval before generation

The agents are deliberately instructed to retrieve Shopify documentation before generating or evaluating Liquid.

This reduces dependence on the model's pretrained knowledge and makes the source of implementation decisions inspectable.

### Separate implementation and QA agents

Implementation and evaluation are separated into different agent workflows.

The implementation agent is responsible for producing a solution. The QA agent receives the proposed solution and evaluates it against the documentation rather than assuming the implementation is correct.

This separation is intended to reduce confirmation bias in the generation process.

### Human approval gate

The implementation is shown to a human before QA is run.

This makes the workflow:

```text
LLM generation → Human review → Independent QA
```

rather than an entirely autonomous code-generation pipeline.

### Structured QA criteria

The QA prompt explicitly separates syntax, completeness, and best-practice checks. This makes the evaluation more interpretable than a single "is this code good?" judgment.

## Limitations

This project is an experimental implementation and should not be treated as a production Shopify deployment system.

In particular:

* Retrieval quality depends on the indexed documentation corpus.
* A retrieved documentation passage does not guarantee that the generated implementation is correct in the context of a particular Shopify theme.
* The QA agent itself is an LLM and therefore is not a formal verifier.
* The current workflow evaluates generated code as text rather than executing it against a Shopify theme.
* The implementation agent can flag unverified syntax but is currently instructed to generate an implementation even when documentation coverage is incomplete.
* The persisted vector index must be rebuilt when the documentation corpus changes.
* API keys and model configuration are external dependencies.

For production use, additional validation would be appropriate, including theme-level testing, deterministic checks, rendering tests, and validation against Shopify's actual theme environment.

## Example Workflow

Given the feature request:

> Display a product's title, price, and vendor on the product page.

The system follows:

```text
Feature request
      │
      ▼
Implementation Agent
      │
      ├── search_shopify_docs
      │
      ▼
Generated Liquid
      │
      ▼
Human Review
      │
      ▼
QA Agent
      │
      ├── Verify product.title
      ├── Verify product.price
      ├── Verify money filter
      ├── Verify product.vendor
      ├── Check feature requirements
      └── Check documented best practices
      │
      ▼
PASS / FAIL + findings
```

## Motivation

The project explores a broader question in LLM-assisted software development:

**Can retrieval and independent agent-based review make LLM-generated code more reliable when working with a domain-specific language and rapidly changing documentation?**

Shopify Liquid is a useful test case because implementations need to account for both general Liquid syntax and Shopify-specific objects, filters, tags, and theme conventions.

The project therefore focuses not only on generating code, but on building a workflow in which generated code can be traced back to documentation and subjected to a separate verification pass.

## References

* [Shopify Liquid](https://github.com/Shopify/liquid) — Shopify's Liquid template engine.
* [Shopify Liquid documentation](https://shopify.dev/docs/api/liquid) — official Liquid documentation.
* [LlamaIndex](https://www.llamaindex.ai/) — document indexing and retrieval.
* [LangGraph](https://www.langchain.com/langgraph) — agent workflow orchestration.
