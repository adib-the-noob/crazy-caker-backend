from pydantic_settings import BaseSettings

class DevSettings(BaseSettings):
    DEBUG: bool = True
    DATABASE_URL: str
    SECRET_KEY: str
    
    class Config:
        env_file = '.env.dev'
        
settings = DevSettings()

print(settings.DATABASE_URL)