
from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker
import models
from database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def create_employ():
    return {"Database":"Created"}
