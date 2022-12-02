from typing import Any, List

from fastapi import APIRouter, Depends

from app import schemas
from app.services.items_service import ItemService

router = APIRouter()


@router.get("/", response_model=List[schemas.Item])
def read_items(
    item_service: ItemService = Depends(),
    skip: int = 0,
    limit: int = 100,
) -> Any:
    """
    Retrieve items.
    """
    return item_service.read_multi(skip=skip, limit=limit)


@router.post("/", response_model=schemas.Item)
def create_item(
    *,
    item_service: ItemService = Depends(),
    item_in: schemas.ItemCreate,
) -> Any:
    """
    Create new item.
    """
    return item_service.create(item_in=item_in)


@router.put("/{id}", response_model=schemas.Item)
def update_item(
    *,
    item_service: ItemService = Depends(),
    id: int,
    item_in: schemas.ItemUpdate,
) -> Any:
    """
    Update an item.
    """
    return item_service.update(id=id, item_in=item_in)


@router.get("/{id}", response_model=schemas.Item)
def read_item(
    *,
    item_service: ItemService = Depends(),
    id: int,
) -> Any:
    """
    Get item by ID.
    """
    return item_service.read(id=id)


@router.delete("/{id}", response_model=schemas.Item)
def delete_item(
    *,
    item_service: ItemService = Depends(),
    id: int,
) -> Any:
    """
    Delete an item.
    """
    return item_service.remove(id=id)
