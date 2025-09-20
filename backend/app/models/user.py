# Simple Pydantic model for quick prototyping; replace with SQLAlchemy for production.
from pydantic import BaseModel

class User(BaseModel):
    id: str
    email: str
