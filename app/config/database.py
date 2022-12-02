from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    """Database settings

    Returns:
        postgres_uri: general form of a connection URI in PostgreSQL
    """

    postgres_host: Optional[str]
    postgres_port: str = "5432"
    postgres_password: Optional[str]
    postgres_user: Optional[str]
    postgres_db: Optional[str]

    @property
    def postgres_uri(self):
        """postgres_uri

        Returns:
            uri: connection URI in PostgreSQL
        """
        return f"postgresql://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"


settings = Settings()
