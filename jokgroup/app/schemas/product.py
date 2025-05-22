from pydantic import BaseModel
from typing import List, Optional


# Shared properties
class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    discount_price: Optional[float] = 0.0
    images: List[str]
    category_id: int
    subcategory_id: int
    colors: List[str]
    sizes: List[str]
    in_stock: bool = True
    rating: Optional[float] = 0.0
    reviews: Optional[int] = 0
    featured: bool = False
    best_seller: bool = False
    new_arrival: bool = False


# For creating a product
class ProductCreate(ProductBase):
    pass


# For outputting a product to the client
class ProductOut(ProductBase):
    id: int
    created_at: Optional[str]

    class Config:
        from_attributes = True
