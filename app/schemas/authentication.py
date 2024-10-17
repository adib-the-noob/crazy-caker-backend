from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    sub: str = None
    id: str = None
    
# class User(BaseModel):
#     email: str
#     full_name: str
#     phone_number: int
#     password: str
#     is_active: bool
#     is_superuser: bool
#     is_verified: bool
#     created_at: str
#     updated_at: str
    
class RegistrationSchema(BaseModel):
    email: str
    full_name: str
    phone_number: int
    password: str
    
class LoginSchema(BaseModel):
    email: str
    password: str