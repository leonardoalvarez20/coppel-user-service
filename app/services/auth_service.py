"""
Handles Auth operations
"""
from fastapi import Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError

from app.helpers.password_hasher import verify_password
from app.helpers.token_generator import create_access_token, decode_token
from app.schemas.user import UserLoginResponse, UserResponse
from app.services.user_service import UserService


class AuthService:
    def __init__(self, user_service: UserService = Depends()):
        self.user_service = user_service

    def authenticate_user(self, username: str, password: str):
        """
        Finds user and validates password
        """
        user = self.user_service.find_user_by_email(username)
        if not user:
            return False
        if not verify_password(password, user.password):
            return False
        return user

    def get_current_user(self, token: str):
        """
        Check if token data is a valid User
        """
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

        try:
            username = decode_token(token=token)
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception

        user = self.user_service.find_user_by_email(email=username)
        if user is None:
            raise credentials_exception

        return jsonable_encoder(UserResponse(**user.dict()))

    def login(self, form_data: OAuth2PasswordRequestForm = Depends()):
        """
        Handles User Login
        """
        user = self.authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        token = create_access_token(data={"sub": user.email})

        return jsonable_encoder(UserLoginResponse(token=token, **user.dict()))
