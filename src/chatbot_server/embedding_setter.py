from llama_index.embeddings.fastembed import FastEmbedEmbedding
from llama_index.core import Settings
from config import FAST_EMBED_MODEL_NAME

class EmbedSettings:
  def __init__(self):
    self.embed_model = FastEmbedEmbedding(model_name=FAST_EMBED_MODEL_NAME)
    self.chunk_size = 256

  def set_and_get_liama_settings(self):
    print("Setting Llama settings...")
    Settings.embed_model = self.embed_model
    Settings.chunk_size = self.chunk_size
    return Settings