from fastapi import APIRouter, Depends, HTTPException,Form, File, UploadFile
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud
from app.schemas import category as category_schema
import os
from uuid import uuid4
import shutil
router = APIRouter()
from app.models import category as catmodel
# ---EGORY ROUTES ---

@router.post("/category/", response_model=category_schema.CategoryOut1)
def create_category(
    name: str = Form(...),
    slug: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # Check if category already exists
    existing = crud.category.get_category_by_name(db, name=name)
    if existing:
        raise HTTPException(status_code=400, detail="Category already exists")

    # Save image with unique name
    extension = os.path.splitext(image.filename)[-1]
    unique_name = f"{uuid4().hex}{extension}"
    image_path = os.path.join("static/images", unique_name)

    with open(image_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    image_url = f"/static/images/{unique_name}"

    # Create category
    new_category = catmodel.Category(name=name, slug=slug, image=image_url)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@router.get("/category/", response_model=list[category_schema.CategoryOut])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.category.get_categories(db, skip=skip, limit=limit)




# --- SUBCATEGORY ROUTES ---

@router.post("/subcategory/", response_model=category_schema.SubCategoryOut)
def create_subcategory(subcategory: category_schema.SubCategoryCreate, db: Session = Depends(get_db)):
    return crud.category.create_subcategory(db=db, subcategory=subcategory)

@router.get("/subcategory/", response_model=list[category_schema.SubCategoryOut])
def read_subcategories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.category.get_subcategories(db, skip=skip, limit=limit)


