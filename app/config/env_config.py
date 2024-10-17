from pydantic_settings import BaseSettings

class DevSettings(BaseSettings):
    DEBUG: bool = True
    DATABASE_URL: str
    
    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 
    
    class Config:
        env_file = '.env.dev'
        
settings = DevSettings()

# print(settings.DATABASE_URL)