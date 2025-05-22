from typing import Optional

from pydantic import BaseModel
from datetime import datetime

class Token(BaseModel):
    access_token: str
    token_type: str
    id: int
    first_name: str
    last_name: str
    email: str
    role: str
    avatar: str | None

class TokenData(BaseModel):
    email: str | None = None


class UserResponse(BaseModel):
    access_token: str
    token_type: str
    id: int
    first_name: str
    last_name: str
    email: str
    role: str
    avatar: Optional[str]  # Optional field for avatar

    class Config:
        orm_mode = True
