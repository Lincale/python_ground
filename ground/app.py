import graphene
from fastapi import FastAPI, Query, Body
from pydantic import BaseModel, Field
from starlette.graphql import GraphQLApp


class User(BaseModel):
    age: int = Field(description="年齢", ge=0)
    name: str = Field(description="氏名")
    country: str = Field(description="出身国")


class GrapheneQuery(graphene.ObjectType):
    # 引数nameを持つフィールドhelloを作成
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    # フィールドhelloに対するユーザへ返すクエリレスポンスを定義
    def resolve_hello(self, info, name):
        return "Hello " + name


app = FastAPI()
app.add_route(
    "/graphql", GraphQLApp(schema=graphene.Schema(query=GrapheneQuery)))


@app.get("/hello")
def hello():
    return {"Hello": "World!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = 'hoge'):
    return {"item_id": item_id, "q": q}


@app.post("/users/{name}", response_model=User)
def create_user(name: str, age: int = Query(None), body: dict = Body(None)):
    return {
        "age": age,
        "name": name,
        "country": body["country"],
    }
