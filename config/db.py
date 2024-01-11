from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ivan:palomeras@fastapimongo-ivanmarcos.ngdijje.mongodb.net/animales"

conn = MongoClient(uri, server_api=ServerApi('1'))