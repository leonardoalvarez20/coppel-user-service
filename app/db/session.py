#!/usr/bin/env python3
"""
Database Handler
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.config.database import settings

engine = settings.postgres_uri
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=create_engine(
        engine,
        isolation_level="REPEATABLE READ",
    ),
)

Base = declarative_base()
