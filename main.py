from augumentation.augument import AugumentedGeneration
from langchain_openai import ChatOpenAI
from langchain_core.prompts import load_prompt
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

youtube_url = "https://www.youtube.com/watch?v=BtdgAys4yMk&list=PLgUwDviBIf0oF6QL8m22w1hIDC1vJ_BHz&index=142"
# Example user query
user_query = "Which traversal algorithm is used in this video? Explain it properly"


augment = AugumentedGeneration(youtube_url, user_query)


# Build vector store from YouTube & web content
augment.build_and_save_vector_store(youtube_url, user_query)

# Load retriever from saved FAISS
retriever = augment.load_and_create_retriever()

# Retrieve relevant chunks
results = retriever.retrieve_texts(user_query)

context = "\n\n".join([res for res in results])

print(context)

model = ChatOpenAI()
prompt = load_prompt('prompts/prompt_template.json')
parser = StrOutputParser()


chain = prompt | model | parser
answer  = chain.invoke({'context': context, 'question': user_query})

print(answer)