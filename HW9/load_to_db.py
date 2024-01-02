import json
from pymongo import MongoClient
from mongoengine import connect
import certifi


uri = "mongodb+srv://vikki1993123:Vikki123%40@cluster0.oricvyp.mongodb.net/testdb?retryWrites=true&w=majority"

client = MongoClient(uri, tlsCAFile=certifi.where())
db = client.testdb
authors_collection = db["authors"]
quotes_collection = db["quotes"]


with open("authors_output.json") as file:
    try:
        
        authors_data_list = [json.loads(line) for line in file if line.strip()]
        authors_collection.insert_many(authors_data_list)
    except json.JSONDecodeError as e:
        print(f"Error loading data from authors_output.json: {e}")


with open("quotes_output.json") as file:
    try:
        quotes_data_list = [json.loads(line) for line in file if line.strip()]
        quotes_collection.insert_many(quotes_data_list)
    except json.JSONDecodeError as e:
        print(f"Error loading data from quotes_output.json: {e}")


client.close()
