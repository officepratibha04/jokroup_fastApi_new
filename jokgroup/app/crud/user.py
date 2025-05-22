from sqlalchemy.orm import Session
from app import models
from app.schemas import user as user_schema
from datetime import datetime
from app.utils.auth import get_user_by_email, hash_password,verify_password

def create_user1(db: Session, user: user_schema.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        role="user",
        avatar="https://example.com/avatars/aarav.jpg",
        password=hashed_password,
        created_at=datetime.utcnow()
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Note  -- 1 crud used in 2 routes as for multitime use

# signup banane me itna time q laga

# do you means in header or body?
