from fastapi import FastAPI
from routers import blogs,users,authentication
import models
from database import engine

models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(authentication.router)
app.include_router(blogs.router)
app.include_router(users.router)