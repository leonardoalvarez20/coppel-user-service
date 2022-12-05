"""
User schemas
"""
from datetime import datetime
from typing import Optional, Union

from bson import ObjectId
from pydantic import BaseModel, Field

from app.schemas.types.pyobjectid import PyObjectId


class UserCreateRequest(BaseModel):
    """
    User request creation attributes
    """

    first_name: str
    last_name: str
    email: str
    age: int
    password: str


class UserBase(BaseModel):
    """
    User Base Attribues
    """

    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    age: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class UserInDBase(UserBase):
    """
    User attributes in DB
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    first_name: str
    last_name: str
    email: str
    age: int
    password: str
    created_at: datetime
    updated_at: datetime


class UserCreateDB(UserBase):
    """
    User Creation Attribues
    """

    first_name: str
    last_name: str
    email: str
    age: int
    password: Union[str, None] = None  # Password hashed
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class UserResponse(UserBase):
    """
    User Response attributes
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class UserLoginResponse(BaseModel):
    """
    User Login Response Attributes
    """

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str = Field(alias="first_name")
    age: int
    token: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
