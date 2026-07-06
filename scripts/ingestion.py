from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
from dotenv import load_dotenv

load_dotenv()

Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")

documents = SimpleDirectoryReader(
    input_dir="../docs",
    recursive=True,
    required_exts=[".md"],
).load_data()

for doc in documents:
    path = doc.metadata.get("file_path", "")
    if "/filters/" in path:
        doc.metadata["doc_type"] = "liquid_filter"
    elif "/objects/" in path:
        doc.metadata["doc_type"] = "liquid_object"
    elif "/tags/" in path:
        doc.metadata["doc_type"] = "liquid_tag"
    else:
        doc.metadata["doc_type"] = "theme_doc"

pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=512, chunk_overlap=80),
        OpenAIEmbedding(model="text-embedding-3-small"),
    ]
)

nodes = pipeline.run(documents=documents)
pipeline.persist("./pipeline_cache")

index = VectorStoreIndex(nodes)
index.storage_context.persist("./storage")

print(f"Indexed {len(nodes)} nodes")