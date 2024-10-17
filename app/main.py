from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.db import Base, engine


@asynccontextmanager
async def init_db(app : FastAPI):
    try:
        Base.metadata.create_all(bind=engine)
        yield
    finally:
        pass
    
app = FastAPI(
    title="CrazyCake Apis",
    description="This project contains apis for CrazyCake",
    version="0.1.0",
    lifespan=init_db
)

async def get_root():
    return {"message": "Hello World"}
