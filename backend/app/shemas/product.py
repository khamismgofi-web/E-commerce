from pydantic import BaseModel, Field, HttpUrl
from typing import Optional, List
from datetime import datetime

# Shared properties across schemas
class ProductBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100, description="The name of the product")
    description: str = Field(..., min_length=10, description="Detailed description of the product")
    price: float = Field(..., gt=0, description="Price must be greater than zero")
    stock: int = Field(..., ge=0, description="Available stock quantity")
    category_id: int = Field(..., description="ID of the category this product belongs to")
    image_url: Optional[HttpUrl] = Field(None, description="Optional URL to the product image")

# Schema for creating a product (Data received from client)
class ProductCreate(ProductBase):
    pass

# Schema for updating a product (All fields optional to support partial updates/PATCH)
class ProductUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = Field(None, min_length=10)
    price: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    category_id: Optional[int] = None
    image_url: Optional[HttpUrl] = None

# Schema for returning a product (Data sent back to client)
class ProductResponse(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        # Allows Pydantic to read data even if it's an ORM model (like SQLAlchemy)
        from_attributes = True