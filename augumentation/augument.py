from ingestion.youtube import YoutubeIngestor
from ingestion.web_search import WebSearch
from utils.splitter import TextSplitter
from utils.Embedding import Embedding
from retriver.retriver import Retriever


class AugumentedGeneration:
    
    def __init__(self, youtube_url, query):
        self.youtube_url = youtube_url
        self.query = query


    def build_and_save_vector_store(self , youtube_url, query):
        # 1. Ingest YouTube transcript
        yt_ingestor = YoutubeIngestor()
        transcript = yt_ingestor.ingest_youtube_video(youtube_url)
        # print("\n🎥 YouTube Transcript Extracted")

        # 2. Perform web search
        web_search = WebSearch()
        web_content = web_search.search_web_with_context(query)
        # print("\n🌐 Web Search Completed")

        # 3. Combine transcript + web content
        combined_text = transcript + "\n\n" + web_content[:400]

        # 4. Split into documents
        splitter = TextSplitter(chunk_size=1000, chunk_overlap=200)
        documents = splitter.create_documents([combined_text])
        print(f"\n Split into {len(documents)} document chunks")

        # 5. Create vector store
        embedder = Embedding(model_name='text-embedding-3-small')
        vector_store = embedder.create_vector_store(documents)

        # 6. Save vector store to disk
        embedder.save_vector_store(vector_store, folder_path="faiss_index/")
        print("\n Vector store saved to 'faiss_index/'")

        return vector_store


    def load_and_create_retriever(self):
        # Load the saved vector store
        embedder = Embedding(model_name='text-embedding-3-small')
        vector_store = embedder.load_vector_store(folder_path="faiss_index/")

        # Create a retriever
        retriever = Retriever(vector_store, search_type="similarity", top_k=10)

        return retriever






# final_prompt = prompt.invoke({'context': context, 'question': user_query})

# # Generate answer using the LLM
# answer = model.invoke(final_prompt)



# res = parser.invoke(answer)

# print(res)