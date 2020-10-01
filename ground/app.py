from fastapi import FastAPI, Query, Body
from pydantic import BaseModel, Field


class User(BaseModel):
    age: int = Field(description="年齢", ge=0)
    name: str = Field(description="氏名")
    country: str = Field(description="出身国")


app = FastAPI()


@app.get("/hello")
def hello():
    return {"Hello": "World!"}


@app.post("/users/{name}", response_model=User)
def create_user(name: str, age: int = Query(None), body: dict = Body(None)):
    return {
        "age": age,
        "name": name,
        "country": body["country"],
    }
