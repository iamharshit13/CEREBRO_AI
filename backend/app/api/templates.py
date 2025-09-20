from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class Template(BaseModel):
    id: str
    name: str
    system_prompt: str
    template: str

# Simple in-memory store
TEMPLATES = []

@router.get('/', response_model=List[Template])
def list_templates():
    return TEMPLATES

@router.post('/', response_model=Template)
def create_template(t: Template):
    TEMPLATES.append(t)
    return t
