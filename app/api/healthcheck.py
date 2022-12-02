"""
App end-points
"""
from fastapi import APIRouter, Response

router = APIRouter()


@router.get("/healthcheck")
def healthcheck():
    """
    Health check end-point
    """
    return Response(content="OK")
