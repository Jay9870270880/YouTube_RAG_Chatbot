class Retriever:
    def __init__(self, vector_store, search_type="similarity", top_k=10):
        """
        Initialize the retriever using a FAISS vector store.

        Args:
            vector_store (FAISS): Loaded FAISS vector store.
            search_type (str): Search type, e.g., 'similarity', 'mmr'.
            top_k (int): Number of results to retrieve.
        """
        # Create retriever from the vector store
        self.retriever = vector_store.as_retriever(
            search_type=search_type,
            search_kwargs={"k": top_k}
        )

    def retrieve_relevant_chunks(self, query):
        """
        Retrieve documents using the retriever pipeline.

        Args:
            query (str): The user query.

        Returns:
            list of Document: List of retrieved Document objects.
        """
        results = self.retriever.invoke(query)

        return results

    def retrieve_texts(self, query):
        """
        Retrieve just the text content of relevant chunks.

        Args:
            query (str): The user query.

        Returns:
            list of str: List of text chunks.
        """
        docs = self.retrieve_relevant_chunks(query)
        return [doc.page_content for doc in docs]

    def retrieve_with_metadata(self, query):
        """
        Retrieve texts with their metadata.

        Returns:
            list of dict: Each containing 'content' and 'metadata'.
        """
        docs = self.retrieve_relevant_chunks(query)
        return [{"page_content": doc.page_content, "metadata": doc.metadata} for doc in docs]
    
    def invoke(self, query):
        """
        Invoke the retriever pipeline to get relevant documents.

        Args:
            query (str): The user query.

        Returns:
            list of Document: List of retrieved Document objects.
        """
        return self.retrieve_relevant_chunks(query )
