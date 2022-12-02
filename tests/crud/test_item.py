from sqlalchemy.orm import Session

from app.db.crud import item as item_crud
from app.schemas.item import ItemCreate, ItemUpdate
from tests.utils.utils import random_lower_string


def test_create_item(db: Session) -> None:
    """Test create a valid item"""
    title = random_lower_string()
    description = random_lower_string()
    item_in = ItemCreate(title=title, description=description)
    item = item_crud.create(db=db, obj_in=item_in)
    assert item.title == title
    assert item.description == description


def test_get_item(db: Session) -> None:
    """Test get an item"""
    title = random_lower_string()
    description = random_lower_string()
    item_in = ItemCreate(title=title, description=description)
    item = item_crud.create(db=db, obj_in=item_in)
    stored_item = item_crud.get(db=db, id=item.id)
    assert stored_item
    assert item.id == stored_item.id
    assert item.title == stored_item.title
    assert item.description == stored_item.description


def test_update_item(db: Session) -> None:
    """Test update an item"""
    title = random_lower_string()
    description = random_lower_string()
    item_in = ItemCreate(title=title, description=description)
    item = item_crud.create(db=db, obj_in=item_in)
    description2 = random_lower_string()
    item_update = ItemUpdate(description=description2)
    item2 = item_crud.update(db=db, db_obj=item, obj_in=item_update)
    assert item.id == item2.id
    assert item.title == item2.title
    assert item2.description == description2


def test_delete_item(db: Session) -> None:
    """Test delete an item"""
    title = random_lower_string()
    description = random_lower_string()
    item_in = ItemCreate(title=title, description=description)
    item = item_crud.create(db=db, obj_in=item_in)
    item2 = item_crud.remove(db=db, id=item.id)
    item3 = item_crud.get(db=db, id=item.id)
    assert item3 is None
    assert item2.id == item.id
    assert item2.title == title
    assert item2.description == description
