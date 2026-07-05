from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.products import router as product_router

# This initializes the FastAPI application
app = FastAPI(
    title="E-Commerce API",
    description="Backend services for the E-Commerce Platform",
    version="1.0.0"
)

# Configure CORS (Cross-Origin Resource Sharing)
# Update allow_origins with your production frontend URL later
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins during development
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Include API Routers
app.include_router(product_router, prefix="/api/v1")

# Root health-check endpoint
@app.get("/", tags=["Health"])
async def root():
    return {
        "status": "healthy",
        "message": "Welcome to the E-Commerce API. Access documentation at /docs"
    }