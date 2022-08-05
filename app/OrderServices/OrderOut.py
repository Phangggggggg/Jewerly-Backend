from fastapi import APIRouter
from pydantic import BaseModel

from ..config.database_connection import database
router = APIRouter(
    prefix="/orderout",
    tags=["orderin"],
    responses={404: {"description": "Not found"}},
)

order_out_collection=database.order_out

operating_cost_collection=database.operating_cost

class OrderOut(BaseModel):
        date: str
        pile: str
        type_gem: str
        amount: str
        value: str
        source: str

@router.get("/")
async def order_out_handler(orderout: OrderOut,jew_cost: int = 0):

    if jew_cost==0:
        order_doc={"date": orderout.date,"pile": orderout.pile,"type_gem":orderout.type_gem,
                "amount":orderout.amount,"value":orderout.value,"source":orderout.source,
                "is_jew":False}
        try:
            order_out_collection.insert_one(order_doc)
            return {"status":"success"}
        except Exception as e:
            return {"status":"failure","excetion":e}
    else:
        order_doc={"date": orderout.date,"pile": orderout.pile,"type_gem":orderout.type_gem,
                "amount":orderout.amount,"value":orderout.value,"source":orderout.source,
                "is_jew":True}
        try:
            insert_result=order_out_collection.insert_one(order_doc)
        except Exception as e:
            return {"status":"failure at step 1","excetion":e}

        operating_doc={"date":orderout.date, "description": "ค่าทำ Jewellery", 
                        "amount": jew_cost,"tags":insert_result.inserted_id}

        try:
            operating_cost_collection.insert_one(operating_doc)
            return {"status":"success"}
        except Exception as e:
            return {"status":"failure at step 2","excetion":e}

