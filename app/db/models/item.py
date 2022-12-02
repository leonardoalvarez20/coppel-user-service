from sqlalchemy import Column, Integer, Text

from app.db.base_class import Base


class Item(Base):
    """Item model"""

    id = Column(Integer, primary_key=True, index=True)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
