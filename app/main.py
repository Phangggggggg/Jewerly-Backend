from typing import Union
from fastapi import FastAPI

from .Router import user

# from .OrderServices import OrderIn,OperatingCost
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from fastapi import  FastAPI
from .schemas import User

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #allow any origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)




@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.post('login')
# def login(user: User):
# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}