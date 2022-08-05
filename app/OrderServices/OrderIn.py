from fastapi import APIRouter
import pymongo
from pydantic import BaseModel

from ..config.database_connection import database
router = APIRouter(
    prefix="/order",
    tags=["orderin"],
    responses={404: {"description": "Not found"}},
)

collection=database.order_in

class OrderIn(BaseModel):
        date: str
        pile: str
        type_gem: str
        amount: str
        value: str
        

@router.put("/orderin")
async def addOrderIn(orderIn: OrderIn):
        order_doc={"date": orderIn.date,"pile": orderIn.pile,"type_gem":orderIn.type_gem,
           "amount":orderIn.amount,"value":orderIn.value}
        try:
            collection.insert_one(order_doc)
            return {"status":"success"}
        except Exception as e:
	        return {"status":"failure","excetion":e}
	