# Cybersecurity RAG System

A Retrieval-Augmented Generation system built with LangChain, ChromaDB, FastAPI and Streamlit.

## Stack
- Ollama (local LLMs)
- LangChain
- ChromaDB
- FastAPI
- Streamlit

## Setup

1. Install Ollama and pull models
ollama pull nomic-embed-text
ollama pull qwen2.5:3b

2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

3. Add PDFs in data/ folder

4. Run pipeline
python embeddings.py
uvicorn app:app --reload
streamlit run ui_streamlit.py

## Architecture
PDFs → Chunks → Embeddings → ChromaDB → FastAPI → Streamlit

## Features
- RAG pipeline
- Source attribution (Task A)
- Conversation memory (Task B)
