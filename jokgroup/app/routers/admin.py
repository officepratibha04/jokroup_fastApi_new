from fastapi import APIRouter, Depends, HTTPException
from pydantic_core.core_schema import model_schema
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import User
from app.schemas import user as user_schema
from app.crud import user as crud
from app.utils.auth import get_current_user

router = APIRouter()

@router.post("/add_user_admin", response_model=user_schema.UserOut)
def add_admin(user: user_schema.UserCreate1, db: Session = Depends(get_db),current_user = Depends(get_current_user)):
    if not current_user.role =="admin":
        raise HTTPException(status_code=403, detail="Access Denied")
    db_user = crud.get_user_by_email(db, username=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user1(db=db, user=user)


