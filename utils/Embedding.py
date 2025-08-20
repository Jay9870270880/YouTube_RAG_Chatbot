from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
import os


class Embedding:
    def __init__(self, model_name='text-embedding-3-small'):
        """
        Initialize the embedding model.

        Args:
            model_name (str): The name of the OpenAI embedding model to use.
        """
        self.embeddings = OpenAIEmbeddings(model=model_name)

    def create_vector_store(self, documents):
        """
        Create a vector store from a list of documents.

        Args:
            documents (list): List of documents to embed.

        Returns:
            FAISS: A FAISS vector store containing the embedded documents.
        """
        return FAISS.from_documents(documents, self.embeddings)
    
    def save_vector_store(self, vector_store, folder_path="faiss_index"):
        """
        Save the FAISS vector store locally.
        """
        os.makedirs(folder_path, exist_ok=True)  # Create directory if missing
        vector_store.save_local(folder_path)


    def load_vector_store(self, folder_path="faiss_index"):
        """
        Load a FAISS vector store from a local directory.
    
        Args:
            folder_path (str): Path to the saved FAISS index.
    
        Returns:
            FAISS: The loaded vector store.
        """
        return FAISS.load_local(
            folder_path,
            self.embeddings,
            allow_dangerous_deserialization=True  # <- Add this
        )
