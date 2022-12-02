import factory

from ..conftest import TestingSessionLocal


class BaseFactory(factory.alchemy.SQLAlchemyModelFactory):
    """BaseFactory
    Add db session for testing and setup `commit` as action taken for persistence
    """

    class Meta:
        sqlalchemy_session = TestingSessionLocal()
        sqlalchemy_session_persistence = "commit"
