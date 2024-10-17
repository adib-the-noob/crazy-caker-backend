from sqlalchemy import Column, String
from datetime import datetime

from database.db import Base

class BaseModelMixin(Base):
    __abstract__ = True
    
    created_at = Column(String, default=datetime.now, nullable=False)
    updated_at = Column(String, default=datetime.now, onupdate=datetime.now, nullable=False)

    def save(self, db):
        db.add(self)
        db.commit()
        db.refresh(self)
        return self