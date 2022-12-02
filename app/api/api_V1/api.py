from fastapi import APIRouter, status

from app.api.api_V1.endpoints import items

"""
Application API routes
"""
api_router = APIRouter()

api_router.include_router(
    items.router,
    prefix="/items",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)
