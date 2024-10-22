from sqladmin import Admin, ModelView
from models.users import (
    User, Otp
)
from models.profiles import Profile

class UserAdmin(ModelView, model=User):
    column_exclude_list = ['password', 'otp', 'created_at', 'updated_at']
    
class OtpAdmin(ModelView, model=Otp):
    column_exclude_list = ['created_at', 'updated_at']
    
class ProfileAdmin(ModelView, model=Profile):
    column_exclude_list = ['created_at', 'updated_at']