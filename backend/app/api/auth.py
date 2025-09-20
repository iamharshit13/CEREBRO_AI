from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class SignupIn(BaseModel):
    email: str
    password: str

@router.post('/signup')
def signup(payload: SignupIn):
    # TODO: implement persistent users
    if not payload.email:
        raise HTTPException(status_code=400, detail='email required')
    return {'status': 'ok', 'email': payload.email}
