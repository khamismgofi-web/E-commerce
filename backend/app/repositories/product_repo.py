from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from typing import List, Optional
from app.models.product import Product  # Adjust this import to match your actual Product model path
from app.schemas.product import ProductCreate, ProductUpdate

class ProductRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(
        self, 
        search: Optional[str] = None, 
        category_id: Optional[int] = None, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[Product]:
        """Fetch all products with optional search, filtering, and pagination."""
        query = select(Product)
        
        # Apply search filter (matches title case-insensitively)
        if search:
            query = query.where(Product.title.ilike(f"%{search}%"))
            
        # Apply category filter
        if category_id:
            query = query.where(Product.category_id == category_id)
            
        # Apply pagination
        query = query.offset(skip).limit(limit)
        
        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_by_id(self, product_id: int) -> Optional[Product]:
        """Fetch a single product by its ID."""
        query = select(Product).where(Product.id == product_id)
        result = await self.db.execute(query)
        return result.scalar_one_or_none()

    async def create(self, obj_in: ProductCreate) -> Product:
        """Create a new product record."""
        db_product = Product(**obj_in.model_dump())
        self.db.add(db_product)
        await self.db.commit()
        await self.db.refresh(db_product)
        return db_product

    async def update(self, product_id: int, obj_in: ProductUpdate) -> Optional[Product]:
        """Partially update an existing product record."""
        update_data = obj_in.model_dump(exclude_unset=True)
        if not update_data:
            return await self.get_by_id(product_id)

        query = (
            update(Product)
            .where(Product.id == product_id)
            .values(**update_data)
            .execution_options(synchronize_session="fetch")
        )
        await self.db.execute(query)
        await self.db.commit()
        return await self.get_by_id(product_id)

    async def delete(self, product_id: int) -> bool:
        """Delete a product record by its ID."""
        query = delete(Product).where(Product.id == product_id)
        result = await self.db.execute(query)
        await self.db.commit()
        return result.rowcount > 0