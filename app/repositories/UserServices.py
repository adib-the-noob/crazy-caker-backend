from sqlalchemy.orm import Session
from models.users import User
from database.db import get_db  # Assuming this provides a scoped session

class UserServices:
    def __init__(self, db: Session):
        self.db = db
    
    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()
    
    def get_user_by_phn(self, phone_number: int) -> User:
        return self.db.query(User).filter(User.phone_number == phone_number).first()
    
    def create_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)  # To get the updated fields (like ID) after commit
        return user
