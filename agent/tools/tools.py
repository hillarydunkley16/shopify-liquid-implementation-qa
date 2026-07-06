from llama_index.core import StorageContext, load_index_from_storage, Settings
from llama_index.embeddings.openai import OpenAIEmbedding
from dotenv import load_dotenv
from langchain_core.tools import tool
import os 
from pathlib import Path
load_dotenv()

Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

# storage_context = StorageContext.from_defaults(persist_dir="../../storage")
# index = load_index_from_storage(storage_context)

# query_engine = index.as_query_engine()

# # response = query_engine.query("What does the assign tag do in Liquid?")

# print(response)
# print("---")
# for node in response.source_nodes:
#     print(node.metadata.get("file_name"), "|", node.metadata.get("doc_type"))
#     print(f"Score: {node.score:.4f}")
#     print(node.text[:300])
#     print()


STORAGE_DIR = Path(__file__).parent.parent.parent / "scripts" / "storage"
print("Loading from:", STORAGE_DIR)

storage_context = StorageContext.from_defaults(persist_dir=str(STORAGE_DIR))
index = load_index_from_storage(storage_context)

# Verify the index actually has content
docstore = storage_context.docstore
# for doc_id, doc in list(docstore.docs.items())[:5]:
#     print(doc.metadata.get("file_name"))
#     print(repr(doc.text[:100]))
#     print()
# found = False

# for doc in docstore.docs.values():
#     filename = doc.metadata.get("file_name")
#     if filename and "assign" in filename.lower():
#         found = True
#         print(filename)
#         print(doc.text[:300])
#         print()

# print("Found:", found)

# retriever = index.as_retriever(similarity_top_k=5)
# nodes = retriever.retrieve("assign")
# for n in nodes:
#     print(n.metadata["file_name"], n.score)
# Run a direct test query before wrapping in the tool
query_engine = index.as_query_engine()
# test = query_engine.query("What does the break tag do in Liquid?")
# print("Test answer:", test)
# for node in test.source_nodes:
#     print(node.metadata.get("file_name"), node.score)

print("Loading from:", STORAGE_DIR)
print("Exists:", STORAGE_DIR.exists())
@tool 
def search_shopify_docs(query: str) -> str:
    """Search Shopify docs for relevant information."""
    print("Searching Shopify docs for query:", query)
    query_engine = index.as_query_engine(similarity_top_k=3)
    response = query_engine.query(query)
    results = []
    for node in response.source_nodes:
        results.append(f"{node.metadata.get('file_name')} | {node.metadata.get('doc_type')}\nScore: {node.score:.4f}\n{node.text[:800]}\n")
    return "\n".join(results)