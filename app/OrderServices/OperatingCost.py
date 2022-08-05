from fastapi import APIRouter
import pymongo
from pydantic import BaseModel 

from ..config.database_connection import database
router = APIRouter(
    prefix="/optCost",
    tags=["optCost"],
    responses={404: {"description": "Not found"}},
)