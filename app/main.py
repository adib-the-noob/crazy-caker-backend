from fastapi import FastAPI
from sqladmin import Admin, ModelView

from contextlib import asynccontextmanager

from database.db import Base, engine
from routers.v1 import (
    authentication_routers
)
from admin.admin_models import (
    UserAdmin,
    OtpAdmin, 
    ProfileAdmin
)

@asynccontextmanager
async def init_db(app : FastAPI):
    try:
        # Base.metadata.create_all(bind=engine)
        yield
    finally:
        pass
    
app = FastAPI(
    title="CrazyCake Apis",
    description="This project contains apis for CrazyCake",
    version="0.1.0",
    lifespan=init_db
)
admin = Admin(
    app=app,
    engine=engine, 
    base_url="/admin",
    title="CrazyCake Admin",
)


@app.get("/root")
async def get_root():
    return {"message": "Hello World"}

# routes
app.include_router(authentication_routers.router)

# admin
admin.add_view(UserAdmin)
admin.add_view(OtpAdmin)
admin.add_view(ProfileAdmin)