from pydantic import BaseModel

class ProfileSchema(BaseModel):
    profile_picture: str
    address : str
    