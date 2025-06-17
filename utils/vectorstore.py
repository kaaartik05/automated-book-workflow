import chromadb
from chromadb.config import Settings
import uuid

client = chromadb.Client(Settings(anonymized_telemetry=False))
collection = client.get_or_create_collection(name="book_versions")


def save_version(chapter_id, text, role="ai-writer"):
    doc_id = str(uuid.uuid4())
    collection.add(
        documents=[text],
        ids=[doc_id],
        metadatas=[{
            "chapter": chapter_id,
            "role": role
        }]
    )
    return doc_id


def search_versions(query, top_k=3):
    return collection.query(query_texts=[query], n_results=top_k)
