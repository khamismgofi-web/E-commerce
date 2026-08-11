"""
Cart endpoints. Every route requires authentication via get_current_user;
the cart is always scoped to the authenticated user, so no user_id or
cart_id is ever taken from the request path or body.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user, get_db
from app.models.user import User
from app.schemas.cart import CartItemAdd, CartItemUpdate, CartResponse
from app.services.cart_service import (
    CartService,
    InsufficientStock,
    ItemNotFound,
    ProductNotFound,
)

router = APIRouter(prefix="/cart", tags=["cart"])


def get_cart_service(db: AsyncSession = Depends(get_db)) -> CartService:
    return CartService(db)


@router.get("", response_model=CartResponse)
async def get_cart(
    current_user: User = Depends(get_current_user),
    service: CartService = Depends(get_cart_service),
):
    return await service.get_cart(current_user.id)


@router.post("/items", response_model=CartResponse, status_code=status.HTTP_201_CREATED)
async def add_item(
    payload: CartItemAdd,
    current_user: User = Depends(get_current_user),
    service: CartService = Depends(get_cart_service),
):
    try:
        return await service.add_item(
            current_user.id, payload.product_id, payload.quantity
        )
    except ProductNotFound:
        raise HTTPException(status_code=404, detail="Product not found")
    except InsufficientStock as e:
        raise HTTPException(
            status_code=400,
            detail=f"Insufficient stock. Only {e.available} unit(s) available.",
        )


@router.put("/items/{item_id}", response_model=CartResponse)
async def update_item_quantity(
    item_id: int,
    payload: CartItemUpdate,
    current_user: User = Depends(get_current_user),
    service: CartService = Depends(get_cart_service),
):
    try:
        return await service.update_quantity(
            current_user.id, item_id, payload.quantity
        )
    except ItemNotFound:
        raise HTTPException(status_code=404, detail="Cart item not found")
    except InsufficientStock as e:
        raise HTTPException(
            status_code=400,
            detail=f"Insufficient stock. Only {e.available} unit(s) available.",
        )


@router.delete("/items/{item_id}", response_model=CartResponse)
async def remove_item(
    item_id: int,
    current_user: User = Depends(get_current_user),
    service: CartService = Depends(get_cart_service),
):
    try:
        return await service.remove_item(current_user.id, item_id)
    except ItemNotFound:
        raise HTTPException(status_code=404, detail="Cart item not found")


@router.delete("", status_code=status.HTTP_204_NO_CONTENT)
async def clear_cart(
    current_user: User = Depends(get_current_user),
    service: CartService = Depends(get_cart_service),
):
    await service.clear_cart(current_user.id)

    