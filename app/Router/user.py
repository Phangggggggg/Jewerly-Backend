
from fastapi import APIRouter,Depends,HTTPException,status
from app.auth.gen_token import create_access_token
from app.auth.hashing import Hash
from app.schemas import UserDisplay,User
from ..config.database_connection import database
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/user',
    tags=['user'],
    responses={404: {"description": "Not found"}},
)
collection=database.user

@router.post('/register',response_model=UserDisplay)
def register(request: User):
    user_doc = {
        'email': request.email,
        'username': request.username,
        'password': Hash.bcrypt(request.password),
        'role': request.role
    }
    if collection.count_documents({"username":request.username})!=0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Username is already existed.")
    else:
        collection.insert_one(user_doc)
        return request
    
@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends()):
     user = collection.find({'username': request.username})
     password=user[0]["password"]
     username=user[0]["username"]
     if not user:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No User")
     if not Hash.verify(password,request.password):
         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Password")
     access_token = create_access_token(data={'username':request.username})
     return {
         'access_token': access_token,
         'token_type': 'bearer',
         'username': username
     }