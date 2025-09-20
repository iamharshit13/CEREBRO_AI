from pydantic import BaseModel
from typing import Optional

class Workspace(BaseModel):
    id: str
    name: str
    system_prompt: Optional[str] = None
