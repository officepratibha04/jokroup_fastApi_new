from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.auth import UserResponse
from app.utils.auth import authenticate_user, create_access_token, get_current_user



router = APIRouter()


@router.post("/login", response_model=UserResponse)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(data={"sub": user["email"]})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        **user
    }

@router.get("/me", response_model=UserResponse)
def read_me(current_user = Depends(get_current_user)):
    return current_user