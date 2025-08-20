# 📺 YouTube Chatbot with Retrieval-Augmented Generation (RAG)

This project implements an **AI-powered YouTube Chatbot** that can ingest YouTube content, extract meaningful insights, and answer user queries using a **Retrieval-Augmented Generation (RAG)** pipeline. The system combines **YouTube ingestion, topic extraction, embeddings, FAISS retrieval, and OpenAI chat models** to provide context-aware responses.

---

## 🚀 Features

* **Ingest YouTube videos** and extract transcripts.
* **Extract topics** for better context understanding.
* **Perform web search** (via Google Serper API) for additional knowledge.
* **Text augmentation** and splitting for improved context handling.
* **Generate embeddings** and store them in **FAISS** (vector database).
* **Retriever** fetches the most relevant chunks for queries.
* **OpenAI ChatModel** generates final responses using retrieved context.
* **Prompt templates** control chatbot personality and behavior.

---

## 📂 Project Structure

```
Youtube_Chatbot/
│── main.py                 # Main entry point
│── requirements.txt        # Dependencies
│
├── augumentation/
│   └── augument.py         # Data augmentation functions
│
├── faiss_index/            # FAISS vector database
│   ├── index.faiss
│   └── index.pkl
│
├── ingestion/              # Data ingestion modules
│   ├── youtube.py          # Extracts transcripts from YouTube
│   ├── extract_topics.py   # Extracts keywords/topics
│   ├── web_search.py       # Uses Google Serper API for web search
│   └── .env                # API keys
│
├── prompts/
│   ├── prompt_generate.py  # Generates chatbot prompts
│   └── prompt_template.json# Stores chatbot prompt templates
│
├── retriver/
│   └── retriver.py         # Retrieves relevant context chunks
│
├── utils/
│   ├── Embedding.py        # Handles OpenAI embeddings
│   ├── splitter.py         # Splits text into smaller chunks
│   └── .env                # API keys
```

---

## ⚙️ Components Explained

### 1️⃣ **Ingestion**

* **`youtube.py`**: Fetches transcripts from YouTube videos using APIs/libraries.
* **`extract_topics.py`**: Extracts topics/keywords from the transcript for indexing.
* **`web_search.py`**: Uses **Google Serper API** to fetch additional information related to extracted topics.

🔑 *Purpose*: Build a rich knowledge base by combining video content with external information.

---

### 2️⃣ **Augmentation (`augument.py`)**

Handles data cleaning, preprocessing, and augmentation of text before indexing. Examples:

* Synonym replacement
* Context expansion
* Noise removal

🔑 *Purpose*: Improve diversity and robustness of the chatbot’s knowledge.

---

### 3️⃣ **Embedding (`Embedding.py`)**

* Uses **OpenAI Embeddings API** to convert text into high-dimensional vectors.
* Each chunk of text is represented as an embedding.

🔑 *Purpose*: Enables similarity search in FAISS.

---

### 4️⃣ **Text Splitter (`splitter.py`)**

* Splits large transcripts/documents into smaller overlapping chunks.
* Ensures context is preserved while avoiding token limit issues.

🔑 *Purpose*: Optimized retrieval and better embeddings.

---

### 5️⃣ **Vector Database (FAISS)**

* Stores embeddings generated from transcripts + external web content.
* Enables **fast similarity search**.

Files:

* `index.faiss`: Stores vector index.
* `index.pkl`: Stores metadata (e.g., mapping chunks back to source).

🔑 *Purpose*: Efficient retrieval of relevant content.

---

### 6️⃣ **Retriever (`retriver.py`)**

* Fetches top-K relevant chunks based on query similarity.
* Uses FAISS similarity search.

🔑 *Purpose*: Ensures chatbot responses are grounded in relevant content.

---

### 7️⃣ **Prompts (`prompt_generate.py`, `prompt_template.json`)**

* Defines chatbot behavior, personality, and style.
* `prompt_generate.py` dynamically generates prompts.
* `prompt_template.json` stores reusable templates.

🔑 *Purpose*: Guide the OpenAI model in generating consistent and controlled responses.

---

### 8️⃣ **Main Application (`main.py`)**

* Loads ingestion modules, embeddings, retriever, and prompts.
* Orchestrates the RAG pipeline:

  1. Ingest data (YouTube + Web Search).
  2. Split text into chunks.
  3. Generate embeddings.
  4. Store/retrieve with FAISS.
  5. Generate response with OpenAI ChatModel.

🔑 *Purpose*: Acts as the entry point for chatbot execution.

---

## 🛠️ Technologies Used

* **Python** (main language)
* **OpenAI API** (ChatModel & Embeddings)
* **Google Serper API** (web search)
* **FAISS** (vector database)
* **LangChain-style utilities** (prompting, retrieval)

---

## 📦 Installation

```bash
# Clone repository
 git clone <repo_url>
 cd Youtube_Chatbot

# Create virtual environment
 python -m venv venv
 source venv/bin/activate  # Linux/Mac
 venv\Scripts\activate     # Windows

# Install dependencies
 pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create `.env` files in root, ingestion, and utils folders:

```ini
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
YOUTUBE_API_KEY=your_youtube_api_key 
```

---

## ▶️ Usage

```bash
python main.py
```

* Enter a query about a YouTube video.
* Chatbot retrieves relevant transcript chunks + external info.
* OpenAI ChatModel generates a context-aware response.

---

## 📊 Workflow Diagram

```
YouTube Video → Transcript → Topic Extraction → Web Search →
Augmentation → Splitter → Embeddings → FAISS Index → Retriever →
Prompt → OpenAI ChatModel → 💬 Response
```

---

## 🔮 Future Improvements

* Support multiple embedding models (e.g., HuggingFace).
* Multi-video ingestion for broader knowledge.
* Fine-tuned chatbot personalities.
* Real-time YouTube video ingestion.

---

## 👨‍💻 Author

Developed for intelligent **YouTube-based Q\&A** using modern NLP and retrieval techniques.
