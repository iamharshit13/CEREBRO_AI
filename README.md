# 🧠 Cerebro AI  
*A GPT + RAG Wrapper with Multi-Niche Tuning*

Cerebro AI is a **full-stack AI project scaffold** that wraps GPT models with **Retrieval-Augmented Generation (RAG)**, customizable prompt templates, and a simple web UI.  

This project is designed as both a **portfolio showcase** and a **foundation for a monetizable SaaS product**.  
Users can create workspaces, upload documents, retrieve contextual knowledge, and generate high-quality outputs tuned to specific domains.

---

## ✨ Features
- 🔑 **Authentication** – basic signup/login (stubbed, extendable to JWT/OAuth).  
- 🗂 **Workspaces** – isolate configs per niche (system prompts + templates).  
- 📝 **Prompt Templates** – save and reuse structured prompts.  
- 📄 **RAG Support** – upload docs → chunk → embed → store in vector DB (stub included).  
- 💬 **Chat UI** – simple conversational interface with streaming-ready backend.  
- 📊 **Analytics Ready** – usage tracking scaffolding included.  
- 💳 **Monetization Ready** – Stripe/subscription integration placeholder.  
- 🐳 **Docker Support** – backend, frontend, and worker containers.  

---

## 🏗️ Project Structure
```
cerebro_ai/
├── backend/          # FastAPI app (API + LLM wrapper + RAG services)
│   ├── app/
│   │   ├── api/      # Routes: auth, chat, templates
│   │   ├── models/   # Pydantic models (stub, replace with SQLAlchemy)
│   │   ├── services/ # LLM adapter + RAG stubs
│   │   └── workers/  # Async ingestion stubs
│   └── requirements.txt
├── frontend/         # Next.js app (chat UI + dashboard)
│   ├── pages/
│   ├── components/
│   └── package.json
├── workers/          # Worker process (stubbed)
├── infrastructure/   # docker-compose & infra as code
└── README.md
```

---

## ⚡ Quick Start

### 1. Backend (FastAPI)
```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows

pip install -r requirements.txt

# Run dev server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Visit API docs at 👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

### 2. Frontend (Next.js)
```bash
cd frontend
npm install
npm run dev
```

Visit 👉 [http://localhost:3000](http://localhost:3000)

---

### 3. Docker (Optional)
Spin up both services with:
```bash
cd infrastructure
docker-compose up --build
```

---

## 🔌 Environment Variables
Backend requires:
```bash
OPENAI_API_KEY=sk-xxxxx
```
If not set, the backend returns **mocked responses** (useful for dev).

---

## 🛠️ Development Workflow
- **Backend**: FastAPI for REST APIs, extend with RAG + database.  
- **Frontend**: Next.js with React hooks for chat and dashboard.  
- **RAG**: Stubbed (`rag.py`) → replace with real ingestion (PyPDF, embeddings, Pinecone/Weaviate/Chroma).  
- **Workers**: Stubbed ingestion worker → expand to Celery/RQ for async jobs.  

---

## 📌 Roadmap
- [ ] Implement document ingestion (PDF/DOCX extraction + chunking).  
- [ ] Connect embeddings to a vector DB (Chroma, Pinecone, or Weaviate).  
- [ ] Add chat history persistence (Postgres + SQLAlchemy).  
- [ ] Add authentication with JWT/OAuth.  
- [ ] Enable streaming responses from OpenAI SDK.  
- [ ] Add analytics dashboard (token usage, latency, costs).  
- [ ] Integrate Stripe for subscriptions.  
- [ ] Deploy backend (Render/AWS) + frontend (Vercel).  

---

## 🚀 Demo Script
1. Start backend + frontend.  
2. Create a workspace (stubbed).  
3. Upload a document (stubbed).  
4. Ask a question in Chat → LLM responds with context.  
5. Show how templates can change tone/structure.  

---

## 🧩 Tech Stack
- **Backend**: FastAPI (Python), Uvicorn  
- **Frontend**: Next.js (React, TypeScript)  
- **Workers**: Python stubs (extendable to Celery/RQ)  
- **Vector DB**: (planned) Pinecone / Weaviate / Chroma  
- **Database**: PostgreSQL (planned, Supabase for quick setup)  
- **Auth**: JWT/OAuth (stubbed, extendable with Clerk/Auth0)  
- **Infra**: Docker Compose, optional Terraform  

---

## 🙌 Contributing
This scaffold is designed for rapid prototyping.  
Pull requests and ideas for expanding Cerebro AI into a full product are welcome!

---

## 📄 License
MIT License © 2025
