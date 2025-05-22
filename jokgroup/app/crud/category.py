from sqlalchemy.orm import Session
from app import models
from app.schemas import category as category_schema
from sqlalchemy import func
def get_category_by_name(db: Session, name: str):
    return db.query(models.Category).filter(name == models.Category.name).first()

def create_category(db: Session, category: category_schema.CategoryCreate):
    db_category = models.Category(name=category.name, slug=category.slug)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

"""def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()"""

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    categories = db.query(models.Category).offset(skip).limit(limit).all()
    results = []

    for category in categories:
        # Count products in category
        total_products = db.query(func.count(models.Product.id)) \
            .filter(models.Product.category_id == category.id).scalar()

        # Prepare subcategories with their product count
        subcategories = []
        for sub in category.subcategories:
            sub_total = db.query(func.count(models.Product.id)) \
                .filter(models.Product.subcategory_id == sub.id).scalar()
            subcategories.append({
                "id": sub.id,
                "name": sub.name,
                "slug": sub.slug,
                "category_id": sub.category_id,
                "total_product": sub_total
            })

        results.append({
            "id": category.id,
            "name": category.name,
            "slug": category.slug,
            "image": category.image,
            "total_product": total_products,
            "subcategories": subcategories
        })

    return results

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(category_id == models.Category.id).first()

def create_subcategory(db: Session, subcategory: category_schema.SubCategoryCreate):
    db_subcategory = models.SubCategory(
        name=subcategory.name,
        slug=subcategory.slug,
        category_id=subcategory.category_id
    )
    db.add(db_subcategory)
    db.commit()
    db.refresh(db_subcategory)
    return db_subcategory

def get_subcategories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.SubCategory).offset(skip).limit(limit).all()

def get_subcategory(db: Session, subcategory_id: int):
    return db.query(models.SubCategory).filter(subcategory_id == models.SubCategory.id).first()
