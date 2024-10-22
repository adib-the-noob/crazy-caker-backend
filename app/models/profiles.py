from database.db import Base
from models.BaseModelMixin import BaseModelMixin

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Profile(BaseModelMixin, Base):
    __tablename__ = "profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    
    user = relationship("User", back_populates="profile")
    user_id = Column(Integer, ForeignKey("users.id"))
    
    profile_picture = Column(String, nullable=False)
    address = Column(String, nullable=False)
    
    def __repr__(self):
        return f"<Profile {self.user_id}>"
    
    def __str__(self):
        return f"{self.user_id}"