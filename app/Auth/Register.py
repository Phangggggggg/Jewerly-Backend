
from fastapi import FastAPI, status, HTTPException
from fastapi.responses import RedirectResponse
from app.schemas import UserOut, UserAuth
# from replit import db
from app.utils import get_hashed_password
from uuid import uuid4
from fastapi import APIRouter
import pymongo


from ..config.database_connection import database
router = APIRouter(
    prefix="/user",
    tags=["register"],
    responses={404: {"description": "Not found"}},
)

db=database.sign_up


@router.put('/signup', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    # querying database to check if user already exist
    user = db.count_documents({"username":data.username})
    if user == 0:
        user = {
        'username': data.username,
        'email': data.email,
        'password': get_hashed_password(data.password),
        'id': str(uuid4())
        }  
    
        db.insert_one(user) 
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exist"
        )   
    # saving user to database
    return user




    