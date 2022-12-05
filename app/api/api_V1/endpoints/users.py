"""
User's Endpoints
"""
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app import schemas
from app.services.auth_service import AuthService
from app.services.user_service import UserService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


router = APIRouter()


@router.post(
    "", response_model=schemas.UserLoginResponse, response_model_by_alias=False
)
def create_user(
    user_in: schemas.UserCreateRequest,
    user_service: UserService = Depends(),
):
    """
    Creates an User
    """
    return user_service.create(user_in=user_in)


@router.get("/me", response_model=schemas.UserResponse)
def find_by_id(
    token: str = Depends(oauth2_scheme), auth_service: AuthService = Depends()
):
    """
    Returns user's info given a token.
    """
    return auth_service.get_current_user(token=token)


@router.post("/login", response_model=schemas.UserLoginResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(),
):
    """
    Login an User.
    """
    return auth_service.login(form_data=form_data)
