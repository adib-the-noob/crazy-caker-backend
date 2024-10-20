import random
from sqlalchemy.orm import Session

from models.users import User, Otp
from database.db import get_db  

class UserServices:
    def __init__(self, db: Session):
        self.db = db
    
    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(
            User.email == email,    
        ).first()
    
    def get_user_by_phn(self, phone_number: int) -> User:
        return self.db.query(User).filter(
            User.phone_number == phone_number,  
        ).first()
    
    def create_user(self, user: User) -> User:
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)  # To get the updated fields (like ID) after commit
        return user


class OtpService:
    def __init__(self, db: Session):
        self.db = db
        
    def generate_otp(self) -> None:
        return random.randint(1000, 9999)
    
    def create_otp(self, otp: str, phone_number: str) -> Otp:
        user = self.db.query(User).filter(User.phone_number == phone_number).first()
        if user is not None:
            otp = Otp(
                phone_number=phone_number,
                otp=otp,
                user_id=user.id
            )
            otp.save(db=self.db)
            return otp
        return None
    
    def get_otp(self, phone_number: str) -> Otp:
        return self.db.query(Otp).filter(Otp.phone_number == phone_number).first()