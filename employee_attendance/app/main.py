from fastapi import FastAPI
from . import models
from .database import engine
from .routers import employee, attendance

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(employee.router)
app.include_router(attendance.router)
