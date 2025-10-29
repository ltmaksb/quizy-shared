from pydantic import BaseModel
from datetime import datetime

from quizy_shared.schemas.user import UserRole


class JWTPayload(BaseModel):
    jti: str
    email: str
    exp: datetime
    role: UserRole
    token_type: str


class JWTToken(BaseModel):
    access_token: str
    token_type: str


class JWTTokens(BaseModel):
    access_token: str
    refresh_token: str