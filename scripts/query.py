from llama_index.core import StorageContext, load_index_from_storage, Settings
from llama_index.embeddings.openai import OpenAIEmbedding
from dotenv import load_dotenv
from llama_index.core.indices.query.query_transform.base import (
    HyDEQueryTransform,
)
from llama_index.core.query_engine import TransformQueryEngine
load_dotenv()

Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

query_engine = index.as_query_engine()
hyde = HyDEQueryTransform(include_original=True)
query_engine = TransformQueryEngine(query_engine, query_transform=hyde)
# print(response := query_engine.query("What does the assign tag do in Liquid?"))
# response = query_engine.query("What does the assign tag do in Liquid?")

# print(response)
# print("---")
# for node in response.source_nodes:
#     print(node.metadata.get("file_name"), "|", node.metadata.get("doc_type"))
#     print(f"Score: {node.score:.4f}")
#     print(node.text[:300])
#     print()