from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

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
    
    # Relationship
    otp = relationship("Otp", back_populates="user")
    
    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"
    
    def __str__(self):
        return f"{self.full_name}"
    

class Otp(BaseModelMixin, Base):
    __tablename__ = "otps"

    id = Column(Integer, primary_key=True, index=True)
    
    phone_number = Column(String)
    otp = Column(String)
    has_used = Column(Boolean, default=False)
    
    user = relationship("User", back_populates="otp")
    user_id = Column(Integer, ForeignKey("users.id"))
    
    def __repr__(self):
        return f"<Otp(phone_number={self.phone_number}, otp={self.otp})>"
    
    def __str__(self):
        return f"{self.phone_number}"