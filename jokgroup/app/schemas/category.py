from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str
    slug: str
    image: str
    total_product:int
class CategoryCreate(CategoryBase):
    pass
class SubCategoryBase(BaseModel):
    name: str
    slug: str
    category_id: int
    total_product: int

class SubCategoryCreate(BaseModel):
    name: str
    slug: str
    category_id: int
"""class CategoryOut(CategoryBase):
    id: int
    subcategories: list[SubCategoryOut]

    class Config:
        from_attributes = True
class SubCategoryOut(SubCategoryBase):
    id: int

    class Config:
        from_attributes = True"""


class SubCategoryOut(BaseModel):
    id: int
    name: str
    slug: str
    category_id: int
    total_product: int

    class Config:
        from_attributes = True


class CategoryOut(BaseModel):
    id: int
    name: str
    slug: str
    image: str
    total_product: int
    subcategories: list[SubCategoryOut]


class CategoryOut1(BaseModel):
    id: int
    name: str
    slug: str
    image: str

    class Config:
        from_attributes = True