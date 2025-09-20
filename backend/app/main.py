from fastapi import FastAPI
from app.api import chat, templates, auth

app = FastAPI(title="Cerebro AI - GPT RAG Wrapper")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])
app.include_router(templates.router, prefix="/templates", tags=["templates"])

@app.get("/")
def root():
    return {"message": "Cerebro AI API is running"}
