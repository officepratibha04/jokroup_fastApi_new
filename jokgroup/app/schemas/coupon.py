from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CouponBase(BaseModel):
    code: str
    description: Optional[str] = None
    discount_type: str  # "percentage" or "fixed"
    discount_value: float
    minimum_purchase: Optional[float] = 0.0
    valid_from: datetime
    valid_to: datetime
    max_uses: Optional[int] = None
    active: bool = True

class CouponCreate(CouponBase):
    pass

class CouponOut(CouponBase):
    id: int
    used_count: int

    class Config:
        from_attributes = True
