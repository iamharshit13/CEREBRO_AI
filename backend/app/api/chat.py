from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_adapter import LLMAdapter

router = APIRouter()
llm = LLMAdapter()

class ChatIn(BaseModel):
    query: str
    workspace_id: str = None

@router.post('/')
def chat_endpoint(payload: ChatIn):
    system = "You are Cerebro AI assistant. Provide helpful, concise answers."
    prompt = f"{system}\nUser: {payload.query}"
    # For now, call LLM adapter directly (no RAG)
    resp = llm.call(prompt)
    return {"response": resp}
