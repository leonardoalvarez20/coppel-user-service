"""
Database settings
"""

from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Database settings

    Returns:
        database_url: general form of a connection URL in MongoDB
    """

    database_url: Optional[str]
    mongo_db: Optional[str]


@lru_cache
def get_db_settings():
    """
    Get settings and keep it in cache
    """
    return Settings()
