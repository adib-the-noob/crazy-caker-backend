from sqlalchemy import Column, Integer, String
from database.db import Base
from models.BaseModelMixin import BaseModelMixin


class User(BaseModelMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    
    name = Column(String)
    phone_number = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    
    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"
    
    def __str__(self):
        return f"{self.name}"
    
    