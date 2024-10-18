from sqlalchemy import Column, Integer, String, Boolean
from database.db import Base
from models.BaseModelMixin import BaseModelMixin


class User(BaseModelMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    
    full_name = Column(String)
    phone_number = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    
    is_verified = Column(Boolean, default=False)
    is_email_verified = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    
    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"
    
    def __str__(self):
        return f"{self.name}"
    
    