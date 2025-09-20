from pydantic import BaseModel
from typing import List

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatHistory(BaseModel):
    workspace_id: str
    messages: List[ChatMessage] = []
