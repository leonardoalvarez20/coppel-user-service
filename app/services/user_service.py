"""
Handles User operations
"""
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from pymongo.errors import DuplicateKeyError

from app.db.database import User
from app.helpers.password_hasher import get_password_hash
from app.helpers.token_generator import create_access_token
from app.schemas import (
    PyObjectId,
    UserCreateDB,
    UserCreateRequest,
    UserInDBase,
    UserLoginResponse,
    UserResponse,
)


class UserService:
    def create(self, user_in: UserCreateRequest):
        """
        Creates an User and response a Login
        """

        user_in.password = get_password_hash(user_in.password)
        user = UserCreateDB(**user_in.dict())

        try:
            user_inserted = User.insert_one(user.dict())
        except DuplicateKeyError as duplicated:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail=duplicated.details,
            )

        response = UserResponse(
            **{"_id": user_inserted.inserted_id, **user_in.dict()}
        )
        token = create_access_token({"sub": response.email})
        return jsonable_encoder(
            UserLoginResponse(token=token, **response.dict())
        )

    def find_user_by_id(self, user_id: PyObjectId):
        """
        Finds an user by id
        """
        user = User.find_one({"_id": user_id})
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User does not exist.",
            )

        return UserResponse(**user)

    def find_user_by_email(self, email: str):
        """
        Finds an user by email
        """
        user = User.find_one({"email": email})
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User does not exist.",
            )
        return UserInDBase(**user)
