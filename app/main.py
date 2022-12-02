"""
Main file for FastAPI App
"""
import uvicorn

import secure
from fastapi import FastAPI, HTTPException, Request, Response
from psycopg2 import OperationalError
from retrying import retry

from app import __version__
from app.api import healthcheck
from app.api.api_V1.api import api_router
from app.config.logger import init_logging
from app.config.settings import settings
from app.db.session import SessionLocal
from app.utils.exceptions import DeployError


secure_headers = secure.Secure()

fastapi_app = FastAPI(
    title="fastapi-template",
    description="Template for FastAPI projects.",
    version=__version__,
)

# Detail logs for development purposes
fastapi_app.add_event_handler("startup", init_logging)


@fastapi_app.middleware("http")
@retry(
    retry_on_result=DeployError.db_starting_up,
    wait_fixed=10000,
    stop_max_attempt_number=3,
)
async def db_session_middleware(request: Request, call_next):
    """
    Stablish DB sessions per request, it retries on DB starting up failure
    - **request**: http request
    - **call_next**: function that will receive the request as a parameter
    Return response
    """
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    except OperationalError as e:
        DeployError.db_starting_up(e)
    finally:
        request.state.db.close()
    return response


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