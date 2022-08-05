import pymongo;

connection_string="mongodb://localhost:27017/"

mongo_client=pymongo.MongoClient(connection_string)

database=mongo_client.JewerlyDb