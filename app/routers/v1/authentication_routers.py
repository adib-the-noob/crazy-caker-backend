import random

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from database.db import get_db
from models.users import User

from repositories.UserServices import (
    UserServices, 
    OtpService
)
from schemas.authentication import (
    
    # Auth
    LoginSchema,
    RegistrationSchema, 
    Token,
    
    # Otp
    OtpPhnVerifySchema
)

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
        
        # otp    
        otp_service = OtpService(db=db)        
        otp = otp_service.generate_otp()
        otp_service.create_otp(otp=otp, phone_number=user.phone_number)

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


@router.post('/verify-user', response_model=None)
async def verify_phone_number(otpRequest: OtpPhnVerifySchema, db: get_db):
    user_services = UserServices(db=db)
    user_data = user_services.get_user_by_phn(phone_number=otpRequest.phone_number)
    
    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    otp_service = OtpService(db=db)
    otp = otp_service.get_otp(phone_number=otpRequest.phone_number)
    
    if not otp:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="OTP not found"
        )
    
    if otp.has_used:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="OTP has already been used"
        )
    
    otp.has_used = True
    otp.save(db=db)
    
    user_data.is_verified = True
    user_data.save(db=db)
    
    return JSONResponse({
        "status": "success",
        "message": "Phone number verified successfully"
    }, status_code=status.HTTP_200_OK)
    

@router.post("/login", response_model=None)
async def user_login(user: LoginSchema, db: get_db):
    user_services = UserServices(db=db)
    user_data = user_services.get_user_by_phn(phone_number=user.phone_number)

    if not user_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Login failed"
        )
        
    if not verify_password(user.password, user_data.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Login failed"
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

