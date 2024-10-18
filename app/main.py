from fastapi import FastAPI
from contextlib import asynccontextmanager
from database.db import Base, engine
from routers.v1 import (
    authentication_routers
)

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


@app.get("/root")
async def get_root():
    return {"message": "Hello World"}

app.include_router(authentication_routers.router)