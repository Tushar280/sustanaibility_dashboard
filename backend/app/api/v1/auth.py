from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import timedelta
from app.core.security import create_token
from app.core.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])

class LoginInput(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(body: LoginInput):
    if body.email.endswith("@company.com") and body.password == "secret":
        access = create_token({"sub": body.email, "scope": "access"}, timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        refresh = create_token({"sub": body.email, "scope": "refresh"}, timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS))
        return {"access_token": access, "refresh_token": refresh, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
