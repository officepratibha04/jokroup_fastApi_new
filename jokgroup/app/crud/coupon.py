from sqlalchemy.orm import Session
from app import models
from app.schemas import coupon as coupon_schema

def get_coupon_by_code(db: Session, code: str):
    return db.query(models.Coupon).filter(models.Coupon.code == code).first()

def create_coupon(db: Session, coupon: coupon_schema.CouponCreate):
    db_coupon = models.Coupon(
        code=coupon.code,
        description=coupon.description,
        discount_type=coupon.discount_type,
        discount_value=coupon.discount_value,
        minimum_purchase=coupon.minimum_purchase,
        valid_from=coupon.valid_from,
        valid_to=coupon.valid_to,
        max_uses=coupon.max_uses,
        active=coupon.active
    )
    db.add(db_coupon)
    db.commit()
    db.refresh(db_coupon)
    return db_coupon

def get_coupons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Coupon).offset(skip).limit(limit).all()
