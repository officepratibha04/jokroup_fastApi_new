from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from app.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), index=True)
    slug = Column(String(250), unique=True, index=True)
    image = Column(String(250))

    # Relationship to SubCategory
    subcategories = relationship(
        "SubCategory", back_populates="category", cascade="all, delete", passive_deletes=True
    )

    # Relationship to Product
    products = relationship(
        "Product", back_populates="category", cascade="all, delete", passive_deletes=True
    )


class SubCategory(Base):
    __tablename__ = "subcategories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    slug = Column(String(250), unique=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"))
    category = relationship("Category", back_populates="subcategories")

    # Relationship to Product
    products = relationship(
        "Product", back_populates="subcategory", cascade="all, delete", passive_deletes=True
    )