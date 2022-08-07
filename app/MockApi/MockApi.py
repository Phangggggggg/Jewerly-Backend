from fastapi import APIRouter
from typing import List
import pymongo
from pydantic import BaseModel 
from ..config.database_connection import database
router = APIRouter(
    prefix="/mock",
    tags=["mockapi"],
    responses={404: {"description": "Not found"}},
)
collection=database.mock_api
class Item(BaseModel):
    date: str
    name: str
    
class MockApi(BaseModel):
    lst: List[Item]

@router.put("/mockapi")
async def addOptCost(mockApi: MockApi ):
        print(mockApi.lst)
        print(mockApi.lst[0].name)
	



