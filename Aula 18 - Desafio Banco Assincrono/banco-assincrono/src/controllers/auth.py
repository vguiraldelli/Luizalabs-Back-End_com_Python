from fastapi import APIRouter
from schemas.auth import LoginIn
from controllers.security import sign_jwt
from views.auth import LoginOut

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=LoginOut)
async def login(login: LoginIn):
    return sign_jwt(user_id=login.user_id)