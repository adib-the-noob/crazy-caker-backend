from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from database.db import get_db
from models.users import User

from repositories.UserServices import UserServices
from schemas.authentication import RegistrationSchema, LoginSchema, Token

from utils.password_utils import get_password_hash, verify_password
from utils.jwt_utils import create_access_token

router = APIRouter(
    tags=["authentication"],
    prefix="/auth/v1"
)

@router.post("/register", response_model=None)
async def register_user(user: RegistrationSchema, db: get_db):
    user_services = UserServices(db=db)
    if user_services.get_user_by_phn(phone_number=user.phone_number):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Registration failed, phone number already exists"
        )
    user = User(
        name=user.full_name,
        phone_number=user.phone_number,
        password=get_password_hash(user.password)
    )
    user_services.create_user(user)    
    return JSONResponse(
        content={"message": "User created successfully", "data": data},
        status_code=status.HTTP_201_CREATED
    )
    

@router.post("/login", response_model=Token)
async def user_login(user: LoginSchema, db: get_db):
    user_services = UserServices(db=db)
    user_data = user_services.get_user_by_email(email=user.email)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    if not verify_password(user.password, user_data.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    access_token = create_access_token(data={"sub": user_data.email})
    token_data = Token(access_token=access_token, token_type="bearer")
    
    return token_data