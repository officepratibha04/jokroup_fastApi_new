from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud
from app.schemas import coupon as coupon_schema

router = APIRouter()

@router.post("/", response_model=coupon_schema.CouponOut)
def create_coupon(coupon: coupon_schema.CouponCreate, db: Session = Depends(get_db)):
    db_coupon = crud.coupon.get_coupon_by_code(db, code=coupon.code)
    if db_coupon:
        raise HTTPException(status_code=400, detail="Coupon code already exists.")
    return crud.coupon.create_coupon(db, coupon=coupon)

@router.get("/", response_model=list[coupon_schema.CouponOut])
def read_coupons(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.coupon.get_coupons(db, skip=skip, limit=limit)
