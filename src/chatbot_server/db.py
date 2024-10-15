from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import QdrantClient

class Db:
    def __init__(self, documents):
        self.client = QdrantClient(path="./db")
        self.vector_store = QdrantVectorStore(client=self.client,collection_name="chat_bot")
        self.storage_context = StorageContext.from_defaults(vector_store=self.vector_store)
        self.documents = documents
        
    def get_index(self):
        return VectorStoreIndex.from_documents(self.documents,storage_context=self.storage_context)