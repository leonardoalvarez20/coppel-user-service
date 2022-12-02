"""
Items Service
"""
from typing import List

from fastapi import HTTPException, status, Depends
from sqlalchemy.orm import Session

from app.db.crud import item
from app.schemas import (
    Item,
    ItemCreate,
    ItemUpdate,
)
from app.helpers.db import get_db

class ItemService: 
    """
    Handles operations for Items
    """

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db         

    def create(self, item_in: ItemCreate) -> Item:
        return item.create(db=self.db, obj_in=item_in)
    
    def update(self, id: int, item_in: ItemUpdate) -> Item:
        item_in_db = item.get(db=self.db, id=id)
        if not item_in_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item {id} not found")
        return item.update(db=self.db, db_obj=item_in_db, obj_in=item_in)

    def remove(self, id: int) -> Item:
        item_in_db = item.get(db=self.db, id=id)
        if not item_in_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item {id} not found")

        return item.remove(db=self.db, id=id)
    
    def read(self,  id: int) -> Item:
        item_in_db = item.get(db=self.db, id=id)
        if not item_in_db:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Item {id} not found")
        return item_in_db

    def read_multi(self, skip: int = 0, limit: int = 100) -> List[Item]:
        return item.get_multi(db=self.db, skip=skip, limit=limit)