from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    
class RegistrationSchema(BaseModel):
    full_name: str
    phone_number: str
    password: str
    
class LoginSchema(BaseModel):
    phone_number: str
    password: str
    
    
class OtpPhnVerifySchema(BaseModel):
    phone_number: str
    otp: str