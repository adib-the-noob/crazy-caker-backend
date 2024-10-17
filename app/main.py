from fastapi import FastAPI

app = FastAPI(
    title="CrazyCake Apis",
    description="This project contains apis for CrazyCake",
    version="0.1.0",
)

async def get_root():
    return {"message": "Hello World"}
