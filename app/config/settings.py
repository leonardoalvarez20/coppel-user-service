from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application Settings
    Store all non specific configurations
    Attributes:
        environment: indicates environment where runs the api (prod, staging, dev)
    """

    environment: Optional[str]
    secret_key: Optional[str]


settings = Settings()
