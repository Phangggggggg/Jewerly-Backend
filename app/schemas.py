from typing import Union

from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str
    
class UserDisplay(BaseModel):
    username: str
    email: str
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class UserInDB(User):
    hashed_password: str

class TokenData(BaseModel):
    username: Union[str, None] = None