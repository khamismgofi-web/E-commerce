from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional

from app.schemas.product import ProductCreate, ProductUpdate, ProductResponse
from app.services.product_service import ProductService
from app.repositories.product_repo import ProductRepository
from app.database import get_db  # Adjust based on your actual database session dependency path

router = APIRouter(prefix="/products", tags=["Products"])

# --- DEPENDENCIES ---

async def get_product_service(db: AsyncSession = Depends(get_db)) -> ProductService:
    """Injects the service layer populated with its repository."""
    repository = ProductRepository(db)
    return ProductService(repository)

async def verify_admin():
    """
    Placeholder dependency for Admin Authentication/Authorization.
    Replace this logic with your JWT/OAuth2 current_user checks.
    """
    # Example structure:
    # if not current_user.is_admin:
    #     raise HTTPException(status_code=403, detail="Admin privileges required")
    pass


# --- ROUTE ENDPOINTS ---

@router.get("", response_model=List[ProductResponse], status_code=status.HTTP_200_OK)
async def list_products(
    search: Optional[str] = Query(None, description="Search products by title case-insensitively"),
    category_id: Optional[int] = Query(None, alias="category", description="Filter products by Category ID"),
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(10, ge=1, le=100, description="Maximum number of records to return"),
    service: ProductService = Depends(get_product_service)
):
    """Fetch a paginated list of products with optional search and category filters."""
    return await service.get_all_products(search=search, category_id=category_id, skip=skip, limit=limit)


@router.get("/{id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def get_product(
    id: int, 
    service: ProductService = Depends(get_product_service)
):
    """Get detailed information about a single product by its ID."""
    return await service.get_product_by_id(product_id=id)


@router.post("", response_model=ProductResponse, status_code=status.HTTP_201_CREATED, dependencies=[Depends(verify_admin)])
async def create_product(
    product_in: ProductCreate, 
    service: ProductService = Depends(get_product_service)
):
    """Create a new product. (Admin Only)"""
    return await service.create_product(obj_in=product_in)


@router.put("/{id}", response_model=ProductResponse, status_code=status.HTTP_200_OK, dependencies=[Depends(verify_admin)])
async def update_product(
    id: int, 
    product_in: ProductUpdate, 
    service: ProductService = Depends(get_product_service)
):
    """Partially update an existing product's fields. (Admin Only)"""
    return await service.update_product(product_id=id, obj_in=product_in)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(verify_admin)])
async def delete_product(
    id: int, 
    service: ProductService = Depends(get_product_service)
):
    """Delete a product by its ID. (Admin Only)"""
    await service.delete_product(product_id=id)
    return None