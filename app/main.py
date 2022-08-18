from typing import Union
from fastapi import FastAPI
from .MockApi import MockApi
from .OrderServices import OrderIn,OperatingCost
from .Auth import Register,Login
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #allow any origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(OrderIn.router)
app.include_router(OperatingCost.router)
app.include_router(MockApi.router)
app.include_router(Register.router)
app.include_router(Login.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}