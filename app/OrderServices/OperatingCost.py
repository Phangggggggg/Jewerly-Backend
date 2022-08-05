from fastapi import APIRouter
import pymongo
from pydantic import BaseModel 

from ..config.database_connection import database
router = APIRouter(
    prefix="/cost",
    tags=["optCost"],
    responses={404: {"description": "Not found"}},
)

collection=database.operating_cost

class OptCost(BaseModel):
        date: str
        description: str
        amount: str

@router.put("/optCost")
async def addOptCost(optCost: OptCost):
        order_doc={"date": optCost.date,"description": optCost.description,"type_gem":optCost.amount}
        try:
            collection.insert_one(order_doc)
            return {"status":"success"}
        except Exception as e:
	        return {"status":"failure","excetion":e}
	

