from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
    
class RegistrationSchema(BaseModel):
    email: str
    full_name: str
    phone_number: int
    password: str
    
class LoginSchema(BaseModel):
    email: str
    password: str