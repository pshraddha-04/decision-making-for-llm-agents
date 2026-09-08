# Setup Guide

## Prerequisites

- Python 3.10 or higher
- Git
- [Ollama](https://ollama.com/download) (for local LLM inference)
- A [Groq API key](https://console.groq.com) (free tier, used by default)

---

## 1. Clone the Repository

```bash
git clone <repo-url>
cd repo
```

---

## 2. Create and Activate Virtual Environment

```bash
python -m venv venv
```

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If you encounter a NumPy/SciPy conflict, run:
> ```bash
> pip install "numpy>=2.0.0,<2.8.0" scipy --upgrade
> ```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=<your_groq_api_key>
```

Get a free Groq API key at https://console.groq.com.

---

## 5. LLM Inference

### Option A — Groq (default, recommended)
No extra setup needed beyond the API key in `.env`.

### Option B — Ollama (local, fallback when Groq limit exceeded)

1. Install Ollama from https://ollama.com/download
2. Pull a model:
```bash
ollama pull llama3.2:3b
```
3. Verify Ollama is running:
```bash
curl http://localhost:11434
```
> Ollama runs as a background service on Windows after install.

---

## 6. Verify Setup

Run the smoke test to confirm all imports work:

```bash
python smoke_test.py
```

Run the FAISS retrieval test to confirm vector search works:

```bash
python faiss_test.py
```

Expected output:
```
Loading embedding model...
Indexing chunks into FAISS...

Query: What programming language is used for data science?

Top 2 results:
  1. Python is a popular programming language for data science.
  2. ...
```

---

## Project Structure

```
repo/
├── README.md           # Project overview and roadmap
├── SETUP.md            # This file
├── requirements.txt    # Python dependencies
├── smoke_test.py       # Import verification script
├── faiss_test.py       # FAISS retrieval verification script
└── .env                # API keys (not committed to git)
```

---

## Notes

- Never commit your `.env` file — add it to `.gitignore`
- Embeddings run locally via `sentence-transformers` (no API key needed)
- For free GPU compute, use [Google Colab](https://colab.research.google.com) or [Kaggle Notebooks](https://www.kaggle.com/code)
