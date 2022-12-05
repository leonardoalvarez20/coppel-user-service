"""
Application API routes
"""
from fastapi import APIRouter, status

from app.api.api_V1.endpoints import users

api_router = APIRouter()

"""
User's routes
"""
api_router.include_router(
    users.router,
    prefix="/users",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)
