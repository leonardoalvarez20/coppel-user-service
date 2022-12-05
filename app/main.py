"""
Main file for FastAPI App
"""
import secure
import uvicorn
from fastapi import FastAPI

from app import __version__
from app.api import healthcheck
from app.api.api_V1.api import api_router
from app.config.logger import init_logging

secure_headers = secure.Secure()

fastapi_app = FastAPI(
    title="fastapi-template",
    description="Template for FastAPI projects.",
    version=__version__,
)

# Detail logs for development purposes
fastapi_app.add_event_handler("startup", init_logging)


@fastapi_app.middleware("http")
async def set_secure_headers(request, call_next):
    """
    Secure headers middleware
    """
    response = await call_next(request)
    secure_headers.framework.fastapi(response)
    return response


fastapi_app.include_router(healthcheck.router)
fastapi_app.include_router(api_router, prefix="/api/v1")

app = fastapi_app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
