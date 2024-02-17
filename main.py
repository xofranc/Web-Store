from fastapi import FastAPI

from pydantic import BaseModel

# uvicorn main:app --reload

app = FastAPI()


@app.get("/")
async def root():
    return {"Aviso":"Saludo de FastAPI"}