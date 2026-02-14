# 🎓 Global University RAG Assistant

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B)
![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-00C4CC)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![License](https://img.shields.io/badge/License-MIT-green)

**An AI-powered Retrieval-Augmented Generation (RAG) system for comprehensive university information retrieval**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Architecture](#-architecture) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Configuration](#-configuration)
- [Architecture](#-architecture)
- [Screenshots](#-screenshots)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🌟 Overview

The **Global University RAG Assistant** is an intelligent information retrieval system that leverages advanced AI technologies to provide accurate, context-aware answers about universities worldwide. Built using Retrieval-Augmented Generation (RAG), it combines web crawling, semantic search, and large language models to deliver comprehensive insights about admissions, programs, scholarships, and more.

### Key Highlights

- 🌍 **50+ Top Universities** from around the world
- 🤖 **AI-Powered Q&A** using Groq LLM (Llama 3.3 70B)
- 🔍 **Semantic Search** with FAISS vector embeddings
- 📊 **Analytics Dashboard** with real-time insights
- 🎨 **Beautiful UI** with custom CSS styling
- ⚡ **Fast & Efficient** vector similarity search

---

## ✨ Features

### 🏛️ University Management
- **Multi-University Selection**: Choose from 50+ top universities globally
- **Geographic Filtering**: Filter by continent, country, or search by name
- **Smart Categorization**: Universities organized by location and ranking

### 🕷️ Intelligent Web Crawling
- **Automated Data Collection**: Crawls official university websites
- **Targeted Extraction**: Focuses on admissions, programs, fees, and research pages
- **Data Validation**: Pydantic-based validation ensures data quality
- **Smart Chunking**: Text segmentation for optimal embedding generation

### 💬 AI-Powered Question Answering
- **Natural Language Queries**: Ask questions in plain English
- **Context-Aware Responses**: Answers backed by retrieved information
- **Source Citations**: Every answer includes source references
- **Multi-University Comparison**: Compare information across institutions

### 📊 Comprehensive Analytics
- **Data Quality Metrics**: Track crawling coverage and document counts
- **Geographic Distribution**: Visualize university distribution by country/continent
- **Performance Indicators**: Monitor vector density and system efficiency
- **Quality Assessment**: AI-powered recommendations for data improvement

### 🎨 Premium User Interface
- **Modern Design**: Gradient backgrounds and smooth animations
- **Responsive Layout**: Works on desktop and tablet devices
- **Interactive Cards**: Beautiful university information cards
- **Real-time Progress**: Live updates during knowledge base building

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | Streamlit | Web application framework |
| **Web Scraping** | BeautifulSoup4, Requests | Content extraction from university websites |
| **Embeddings** | Sentence Transformers | Text vectorization (all-MiniLM-L6-v2) |
| **Vector Store** | FAISS | Efficient similarity search |
| **LLM** | Groq API (Llama 3.3 70B) | Natural language generation |
| **Validation** | Pydantic | Data validation and parsing |
| **Language** | Python 3.8+ | Core programming language |

---

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Groq API key ([Get one here](https://console.groq.com/))

### Step-by-Step Guide

1. **Clone the repository**
   ```bash
   git clone https://github.com/Neelanjan2448040/global-university-rag.git
   cd global-university-rag