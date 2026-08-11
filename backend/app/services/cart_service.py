"""
Business logic for the cart: stock validation and server-side price
calculation. Nothing here talks to HTTP; it raises plain exceptions that
the API layer translates into HTTP responses.
"""
from decimal import Decimal

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.cart import Cart, CartItem
from app.repositories.cart_repo import CartRepository
from app.schemas.cart import CartItemResponse, CartResponse


class CartError(Exception):
    """Base class for cart errors the API layer knows how to handle."""


class ProductNotFound(CartError):
    pass


class InsufficientStock(CartError):
    def __init__(self, available: int):
        self.available = available
        super().__init__(f"Only {available} unit(s) available")


class ItemNotFound(CartError):
    pass


class CartService:
    def __init__(self, db: AsyncSession):
        self.db = db
        self.repo = CartRepository(db)

    async def _to_response(self, cart: Cart) -> CartResponse:
        items = []
        total = Decimal("0")
        for item in cart.items:
            line_total = item.product.price * item.quantity
            total += line_total
            items.append(
                CartItemResponse(
                    id=item.id,
                    product_id=item.product_id,
                    product_name=item.product.name,
                    unit_price=item.product.price,
                    quantity=item.quantity,
                    line_total=line_total,
                )
            )
        return CartResponse(id=cart.id, items=items, total=total)

    async def get_cart(self, user_id: int) -> CartResponse:
        cart = await self.repo.get_or_create_cart(user_id)
        return await self._to_response(cart)

    async def add_item(
        self, user_id: int, product_id: int, quantity: int
    ) -> CartResponse:
        cart = await self.repo.get_or_create_cart(user_id)

        product = await self.repo.get_product(product_id)
        if product is None:
            raise ProductNotFound()

        existing = await self.repo.get_item_by_product(cart.id, product_id)
        desired_qty = quantity + (existing.quantity if existing else 0)

        if desired_qty > product.stock_quantity:
            raise InsufficientStock(available=product.stock_quantity)

        if existing:
            await self.repo.update_qty(existing, desired_qty)
        else:
            await self.repo.add_item(cart.id, product_id, quantity)

        await self.db.commit()
        cart = await self.repo.get_or_create_cart(user_id)
        return await self._to_response(cart)

    async def update_quantity(
        self, user_id: int, item_id: int, quantity: int
    ) -> CartResponse:
        cart = await self.repo.get_or_create_cart(user_id)
        item = await self.repo.get_item(cart.id, item_id)
        if item is None:
            raise ItemNotFound()

        product = await self.repo.get_product(item.product_id)
        if quantity > product.stock_quantity:
            raise InsufficientStock(available=product.stock_quantity)

        await self.repo.update_qty(item, quantity)
        await self.db.commit()

        cart = await self.repo.get_or_create_cart(user_id)
        return await self._to_response(cart)

    async def remove_item(self, user_id: int, item_id: int) -> CartResponse:
        cart = await self.repo.get_or_create_cart(user_id)
        item = await self.repo.get_item(cart.id, item_id)
        if item is None:
            raise ItemNotFound()

        await self.repo.remove_item(item)
        await self.db.commit()

        cart = await self.repo.get_or_create_cart(user_id)
        return await self._to_response(cart)

    async def clear_cart(self, user_id: int) -> None:
        cart = await self.repo.get_or_create_cart(user_id)
        await self.repo.clear_cart(cart)
        await self.db.commit()