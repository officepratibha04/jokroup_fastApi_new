from sqlalchemy import Column, Integer, String, Float, Boolean, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base
from .category import *
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    price = Column(Float, nullable=False)
    discount_price = Column(Float, default=0.0)
    images = Column(Text)  # JSON string
    colors = Column(Text)  # JSON string
    sizes = Column(Text)   # JSON string
    in_stock = Column(Boolean, default=True)
    rating = Column(Float, default=0.0)
    reviews = Column(Integer, default=0)
    featured = Column(Boolean, default=False)
    best_seller = Column(Boolean, default=False)
    new_arrival = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))
    subcategory_id = Column(Integer, ForeignKey("subcategories.id", ondelete="CASCADE"))

    category = relationship("Category", back_populates="products")
    subcategory = relationship("SubCategory", back_populates="products")
