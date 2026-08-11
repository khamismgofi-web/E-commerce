"""
Data access layer for the cart. No business rules here (no stock checks,
no price math) — that belongs in cart_service.py. This layer only knows
how to read/write rows.
"""
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.models.cart import Cart, CartItem
from app.models.product import Product


class CartRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_or_create_cart(self, user_id: int) -> Cart:
        """Every user has exactly one cart, created lazily on first use."""
        result = await self.db.execute(
            select(Cart)
            .where(Cart.user_id == user_id)
            .options(selectinload(Cart.items).selectinload(CartItem.product))
        )
        cart = result.scalar_one_or_none()
        if cart is None:
            cart = Cart(user_id=user_id)
            self.db.add(cart)
            await self.db.flush()
            await self.db.refresh(cart, attribute_names=["items"])
        return cart

    async def get_item(self, cart_id: int, item_id: int) -> CartItem | None:
        result = await self.db.execute(
            select(CartItem).where(
                CartItem.id == item_id, CartItem.cart_id == cart_id
            )
        )
        return result.scalar_one_or_none()

    async def get_item_by_product(
        self, cart_id: int, product_id: int
    ) -> CartItem | None:
        result = await self.db.execute(
            select(CartItem).where(
                CartItem.cart_id == cart_id, CartItem.product_id == product_id
            )
        )
        return result.scalar_one_or_none()

    async def get_product(self, product_id: int) -> Product | None:
        result = await self.db.execute(
            select(Product).where(Product.id == product_id)
        )
        return result.scalar_one_or_none()

    async def add_item(self, cart_id: int, product_id: int, quantity: int) -> CartItem:
        item = CartItem(cart_id=cart_id, product_id=product_id, quantity=quantity)
        self.db.add(item)
        await self.db.flush()
        await self.db.refresh(item, attribute_names=["product"])
        return item

    async def update_qty(self, item: CartItem, quantity: int) -> CartItem:
        item.quantity = quantity
        await self.db.flush()
        return item

    async def remove_item(self, item: CartItem) -> None:
        await self.db.delete(item)
        await self.db.flush()

    async def clear_cart(self, cart: Cart) -> None:
        for item in list(cart.items):
            await self.db.delete(item)
        await self.db.flush()