from pydantic_settings import BaseSettings

class DevSettings(BaseSettings):
    DEBUG: bool = True
    DATABASE_URL: str = 'sqlite:///db.sqlite3'
    SECRET_KEY: str
    
    class Config:
        env_file = '.env.dev'
        
dev_settings = DevSettings()

