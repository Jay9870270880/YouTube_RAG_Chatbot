from langchain_text_splitters import RecursiveCharacterTextSplitter

class TextSplitter:

    def __init__(self, chunk_size=1024, chunk_overlap=128):
        """
        Args:
            chunk_size (int): Max characters in each chunk.
            chunk_overlap (int): Overlap between chunks to preserve context.
        """
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", ".", " ", ""]
        )

    def split_text(self, text):
        """
        Splits the input text into smaller chunks.

        Args:
            text (str): The text to split.

        Returns:
            list of str: List of text chunks.
        """
        return self.splitter.split_text(text)
    
    def create_documents(self, text_list):
        """
        Creates documents from a list of text strings.

        Args:
            text_list (list of str): List of text strings to convert into documents.

        Returns:
            list of Document: List of Document objects.
        """
        return self.splitter.create_documents(text_list)
