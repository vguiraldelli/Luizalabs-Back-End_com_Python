from pydantic import BaseModel
import time, jwt
from typing import Annotated
from uuid import uuid4
from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPBearer
from typing import Annotated

SECRET = "my-secret-key"
ALGORITHM = "HS256"

class AccessToken(BaseModel):
    iss: str
    sub: str
    aud: str
    exp: float
    iat: float
    nbf: float
    jti: str    
    
class JWTToken(BaseModel):
    access_token: AccessToken

def sign_jwt(user_id: str) -> dict:
    token = jwt.encode(
        {
            "iss": "http://localhost:8000",
            "sub": user_id,
            "aud": "curso-fastapi",
            "exp": time.time() + 3600,
            "iat": time.time(),
            "nbf": time.time(),
            "jti": str(uuid4())
        },
        SECRET,
        ALGORITHM
    )
    return {"token": token}
    

async def decode_jwt(token: str) -> JWTToken | None:
    try:
        decoded_token = jwt.decode(token, SECRET, audience="curso-fastapi", algorithms=[ALGORITHM])
        _token = JWTToken.model_validate({"access_token": decoded_token})
        return _token if _token.access_token.exp >= time.time() else None
    except jwt.PyJWTError:
        return None
    
class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool=True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> JWTToken:
        authorization = request.headers.get("Authorization", "")
        scheme, _, credentials = authorization.partition(" ")
        
        if credentials:
            if not scheme == "Bearer":
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Missing or invalid authentication scheme.")

            payload = await decode_jwt(credentials)
            if not payload:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid or expired token.")
            return payload
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid authorization code.")

async def get_current_user(token: Annotated[JWTToken, Depends(JWTBearer())]) -> dict[str, int]:
    return {"user_id": token.access_token.sub}

def login_required(current_user: Annotated[dict[str, int], Depends(get_current_user)]):
    if not current_user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Access denied.")
    return current_user