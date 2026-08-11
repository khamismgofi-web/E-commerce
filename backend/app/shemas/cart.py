"""
Pydantic schemas for cart endpoints.

Assumption: Product price is stored as Decimal in the DB (Numeric column).
"""
from decimal import Decimal

from pydantic import BaseModel, Field, ConfigDict


class CartItemAdd(BaseModel):
    """Payload for POST /cart/items"""
    product_id: int
    quantity: int = Field(gt=0, description="Must be a positive integer")


class CartItemUpdate(BaseModel):
    """Payload for PUT /cart/items/{item_id}"""
    quantity: int = Field(gt=0, description="Must be a positive integer")


class CartItemResponse(BaseModel):
    """A single line item in the cart, with server-computed line total."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    product_id: int
    product_name: str
    unit_price: Decimal
    quantity: int
    line_total: Decimal


class CartResponse(BaseModel):
    """Full cart payload returned by GET /cart."""
    model_config = ConfigDict(from_attributes=True)

    id: int
    items: list[CartItemResponse]
    total: Decimal