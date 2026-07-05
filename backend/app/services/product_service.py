from typing import List, Optional
from fastapi import HTTPException, status
from app.repositories.product_repo import ProductRepository
from app.schemas.product import ProductCreate, ProductUpdate
from app.models.product import Product

class ProductService:
    def __init__(self, product_repo: ProductRepository):
        self.product_repo = product_repo

    async def get_all_products(
        self, 
        search: Optional[str] = None, 
        category_id: Optional[int] = None, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Product]:
        """Fetch products with optional filtering and search."""
        return await self.product_repo.get_all(
            search=search, 
            category_id=category_id, 
            skip=skip, 
            limit=limit
        )

    async def get_product_by_id(self, product_id: int) -> Product:
        """Fetch a single product and raise a 404 error if not found."""
        product = await self.product_repo.get_by_id(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with ID {product_id} not found"
            )
        return product

    async def create_product(self, obj_in: ProductCreate) -> Product:
        """Handle business rules for creating a product."""
        # You can add additional business validation here (e.g., checking if category exists)
        return await self.product_repo.create(obj_in)

    async def update_product(self, product_id: int, obj_in: ProductUpdate) -> Product:
        """Ensure the product exists before attempting to update it."""
        # Check existence first to raise a proper 404 error if it doesn't exist
        await self.get_product_by_id(product_id)
        
        updated_product = await self.product_repo.update(product_id, obj_in)
        return updated_product

    async def delete_product(self, product_id: int) -> None:
        """Ensure the product exists before attempting to delete it."""
        await self.get_product_by_id(product_id)
        await self.product_repo.delete(product_id)