"""
Item Schema
"""
from typing import Optional

import pendulum
from pydantic import BaseModel
from pydantic.schema import datetime


# Shared properties
class ItemBase(BaseModel):
    """Item base schema"""

    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class ItemCreate(ItemBase):
    """Item create schema"""

    title: str


# Properties to receive on item update
class ItemUpdate(ItemBase):
    """Item update schema"""

    pass


# Properties shared by models stored in DB
class ItemInDBBase(ItemBase):
    """Item DB schema"""

    id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True


# Properties to return to client
class Item(ItemInDBBase):
    """Item schema"""

    pass


# Properties properties stored in DB
class ItemInDB(ItemInDBBase):
    pass
