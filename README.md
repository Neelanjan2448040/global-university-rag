# 🎓 Global University RAG Assistant

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/LLM-Groq%20Llama%203.3-orange.svg)](https://groq.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**An intelligent RAG-based retrieval system for global higher education insights.**

[Overview](#-overview) • [Features](#-features) • [Tech Stack](#-tech-stack) • [Installation](#-installation) • [Usage](#-usage)

---

</div>

## 🌟 Overview

The **Global University RAG Assistant** is an intelligent information retrieval system that leverages advanced AI technologies to provide accurate, context-aware answers about universities worldwide. Built using **Retrieval-Augmented Generation (RAG)**, it combines web crawling, semantic search, and large language models to deliver comprehensive insights about admissions, programs, scholarships, and more.

### Key Highlights
- 🌍 **50+ Top Universities** from around the world.
- 🤖 **AI-Powered Q&A** using Groq LLM (Llama 3.3 70B).
- 🔍 **Semantic Search** with FAISS vector embeddings.
- 📊 **Analytics Dashboard** for real-time data insights.
- 🎨 **Premium UI** built with Streamlit and custom CSS.

---

## ✨ Features

### 🏛️ University Management
- **Multi-University Selection**: Choose from 50+ top universities globally.
- **Geographic Filtering**: Filter by continent, country, or search by name.
- **Smart Categorization**: Universities organized by location and ranking.

### 🕷️ Intelligent Web Crawling
- **Automated Data Collection**: Crawls official university websites using BeautifulSoup4.
- **Data Validation**: Pydantic-based validation ensures high-quality input.
- **Smart Chunking**: Optimized text segmentation for embedding generation.

### 💬 AI-Powered Question Answering
- **Natural Language Queries**: Ask questions in plain English.
- **Context-Aware Responses**: Answers backed by retrieved documentation.
- **Source Citations**: Transparency with direct source references for every answer.

### 📊 Comprehensive Analytics
- **Visual Metrics**: Distribution maps and data quality charts.
- **Performance Monitoring**: Track vector density and retrieval efficiency.

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit | Web application framework |
| **Scraping** | BeautifulSoup4 | Content extraction & parsing |
| **Embeddings** | Sentence Transformers | Text vectorization (`all-MiniLM-L6-v2`) |
| **Vector Store** | FAISS | High-speed similarity search |
| **LLM** | Groq API | Llama 3.3 70B inference |
| **Validation** | Pydantic | Schema enforcement |

---

## 📦 Installation

### Prerequisites
- Python 3.8+
- [Groq API Key](https://console.groq.com/)

### Step-by-Step Guide

1. **Clone the repository**
   ```bash
   git clone [https://github.com/YourUsername/global-university-rag.git](https://github.com/YourUsername/global-university-rag.git)
   cd global-university-rag

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt

4. **Environment Configuration**
Create a .env file in the root directory:
   ```bash
   GROQ_API_KEY=your_api_key_here

---

## 🚀 Usage

1. **Launch the Application**
   ```bash
   streamlit run app.py

2. **Select Universities:** Use the sidebar to pick the institutions you want to query.
3. **Build Knowledge Base:** Click the "Initialize" button to crawl and index data.
4. **Ask Away:** Type your query (e.g., "What are the PhD requirements for Stanford?") in the chat interface.

---

## 📁 Project Structure

```bash
├── app.py                # Main Streamlit application
├── components/           # UI components and layouts
├── core/
│   ├── crawler.py        # Web scraping logic
│   ├── engine.py         # RAG & LLM integration
│   └── vector_store.py   # FAISS indexing
├── data/                 # Local cache & university list
├── utils/                # Helpers & validation schemas
├── .env                  # Environment variables
└── requirements.txt      # Project dependencies
