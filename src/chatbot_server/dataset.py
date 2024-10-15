from llama_index.core import SimpleDirectoryReader
from llama_index.readers.file import PagedCSVReader
from config import DATASET
class DataSetter:
  def __init__(self):
    self.dataset_dir = DATASET

  def load_dataset(self):
    print("Loading dataset...")
    csv_reader = PagedCSVReader()
    
    reader = SimpleDirectoryReader( 
        input_files=[self.dataset_dir],
        file_extractor= {".csv": csv_reader}
        )

    docs = reader.load_data()
    return docs