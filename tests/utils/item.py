from typing import Optional

from sqlalchemy.orm import Session

from app.db.crud import item
from app.db.models import Item
from app.schemas.item import ItemCreate
from tests.utils.utils import random_lower_string


def create_random_item(db: Session) -> Item:
    """Create a random item"""
    title = random_lower_string()
    description = random_lower_string()
    item_in = ItemCreate(title=title, description=description, id=id)
    return item.create(db=db, obj_in=item_in)
