
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
from mongoengine import connect


uri = "mongodb+srv://vikki1993123:Vikki123%40@cluster0.oricvyp.mongodb.net/testdb?retryWrites=true&w=majority"


client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
db = client.testdb

# Set up the default connection for MongoEngine
connect(db='testdb', alias='default', host=uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

try:
    # to check if the connection is successful
    client.admin.command('ping')
    print('Successfully connected to DB')
except Exception as e:
    print(e)

