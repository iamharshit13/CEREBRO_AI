# Cerebro AI - GPT RAG Wrapper (Scaffold)

This scaffold contains a minimal starting point for Cerebro AI — a GPT-wrapper with RAG support.
Use this as a foundation to build the full product.

Structure:
- backend: FastAPI app with simple chat route and LLM adapter
- frontend: Next.js pages (lightweight) for chat and dashboard
- workers: Celery worker stub for ingestion/embeddings
- infrastructure: docker-compose for local dev

## Quick start (Backend)
1. Create a Python virtualenv and install deps:
   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Set env var `OPENAI_API_KEY` (or leave empty for mocked responses).
3. Run:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

## Quick start (Frontend - dev)
The frontend is a Next.js scaffold. Install node dependencies and run dev server:
```bash
cd frontend
npm install
npm run dev
```

## Notes
- The LLM calls are basic; replace with your provider SDK and streaming logic.
- This scaffold intentionally keeps things simple to let you iterate quickly.
