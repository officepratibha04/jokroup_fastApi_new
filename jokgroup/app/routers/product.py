import json
import os
import time
from fastapi import APIRouter, UploadFile, File, Form, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.product import Product
from app.schemas.product import ProductOut

router = APIRouter(
    prefix="/api/v1/product",
    tags=["Products"]
)

@router.post("/create")
async def create_product(
    name: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    discount_price: float = Form(0),
    category_id: int = Form(...),
    subcategory_id: int = Form(...),
    colors: str = Form(...),     # Expecting: "red,blue,green"
    sizes: str = Form(...),      # Expecting: "S,M,L"
    in_stock: bool = Form(True),
    rating: float = Form(0.0),
    reviews: int = Form(0),
    featured: bool = Form(False),
    best_seller: bool = Form(False),
    new_arrival: bool = Form(False),
    images: List[UploadFile] = File(...),
    db: Session = Depends(get_db)
):
    # Make sure static/products exists
    upload_folder = "static/products"
    os.makedirs(upload_folder, exist_ok=True)

    # Save images and collect paths
    image_paths = []
    for image in images:
        filename = f"{time.time()}_{image.filename}"
        file_path = os.path.join(upload_folder, filename)

        with open(file_path, "wb") as f:
            f.write(await image.read())

        image_paths.append(f"/{file_path}")  # Save path for DB

    # Convert colors & sizes strings to lists
    color_list = [color.strip() for color in colors.split(",")]
    size_list = [size.strip() for size in sizes.split(",")]

    # Create Product instance
    new_product = Product(
        name=name,
        description=description,
        price=price,
        discount_price=discount_price,
        images=json.dumps(image_paths),   # Store as JSON string
        category_id=category_id,
        subcategory_id=subcategory_id,
        colors=json.dumps(color_list),
        sizes=json.dumps(size_list),
        in_stock=in_stock,
        rating=rating,
        reviews=reviews,
        featured=featured,
        best_seller=best_seller,
        new_arrival=new_arrival,
    )

    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return {"message": "Product created successfully!", "product_id": new_product.id}

@router.get("/list", response_model=List[ProductOut])
def get_products(db: Session = Depends(get_db)):
    products = db.query(Product).all()

    # Convert JSON strings back to Python lists
    for product in products:
        product.images = json.loads(product.images) if product.images else []
        product.colors = json.loads(product.colors) if product.colors else []
        product.sizes = json.loads(product.sizes) if product.sizes else []
        product.created_at = product.created_at.strftime("%Y-%m-%d %H:%M:%S") if product.created_at else None

    return products



## Set your Git username
