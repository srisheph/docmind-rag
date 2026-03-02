# 📄 DocMind – AI-powered PDF Question Answering System (RAG)

DocMind is a Retrieval-Augmented Generation (RAG) based application that allows users to upload PDF documents and ask questions about their content. The system uses semantic search with a vector database and Large Language Models (LLMs) to generate accurate, context-aware answers.

---

## 🚀 Features

* 📂 Upload any PDF document
* 🔍 Semantic search using vector embeddings
* 🤖 Context-aware answers powered by LLMs
* 🧠 Query transformation for improved retrieval accuracy
* 📑 Supports large documents (1000+ pages)
* 🌐 Interactive web UI using Streamlit
* 🐳 Vector database managed with Docker (Qdrant)

---

## 🏗 Architecture

1. **PDF Loader** – Loads and parses uploaded documents
2. **Text Chunking** – Splits documents into overlapping chunks
3. **Embedding Generation** – Converts chunks into vector embeddings
4. **Vector Database (Qdrant)** – Stores and retrieves relevant chunks
5. **Query Transformation** – Refines user queries for better semantic search
6. **LLM Response Generation** – Generates answers using retrieved context
7. **Streamlit UI** – User interface for upload and Q&A

---

## 🛠 Tech Stack

* **Language:** Python
* **Frameworks:** LangChain, Streamlit
* **LLM:** OpenAI GPT models
* **Vector Database:** Qdrant
* **Containerization:** Docker
* **Deployment:** Hugging Face Spaces / Railway (optional)

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/docmind-rag.git
cd docmind-rag
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set environment variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## 🐳 Run Qdrant using Docker

```bash
docker-compose -f docker-compose.db.yml up
```

Qdrant will run on:

```
http://localhost:6333
```

---

## ▶️ Run the application

```bash
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

## 🧪 How It Works

1. Upload a PDF document
2. The document is split into chunks and indexed into Qdrant
3. Enter a question related to the document
4. The system retrieves the most relevant chunks
5. LLM generates an answer using retrieved context

---

## 📁 Project Structure

```
.
├── app.py
├── rag.py
├── requirements.txt
├── docker-compose.db.yml
├── README.md
├── .gitignore
└── docs/
```
## 👨‍💻 Author

**Shephali Srivastava**
GenAI Enthusiast | Machine Learning Learner

GitHub: [https://github.com/your-username](https://github.com/srisheph/)

---

## 📜 License

This project is licensed under the MIT License.

---
