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
    try:
        user_services = UserServices(db=db)
        if user_services.get_user_by_phn(phone_number=user.phone_number):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Registration failed, phone number already exists"
            )
        user = User(
            full_name=user.full_name,
            phone_number=user.phone_number,
            password=get_password_hash(user.password)
        )
        user_services.create_user(user)    
        return JSONResponse(
            content={
                "status": "success",
                "message": "User created successfully, please verify your phone number",
                "data": {
                    "id": user.id,
                    "phone_number": user.phone_number
                }
            },
            status_code=status.HTTP_201_CREATED
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred : {str(e)}"
        )    


@router.post("/login", response_model=None)
async def user_login(user: LoginSchema, db: get_db):
    user_services = UserServices(db=db)
    user_data = user_services.get_user_by_phn(phone_number=user.phone_number)

    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Credentials"
        )
        
    if not verify_password(user.password, user_data.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid Credentials"
        )

    access_token = create_access_token(data={"sub": user_data.email})
    token_data = Token(access_token=(access_token), token_type="bearer")
    
    return JSONResponse(
        content={
            "message": "User login successful",
            "token": token_data.model_dump()
        },
        status_code=status.HTTP_200_OK
    )    

