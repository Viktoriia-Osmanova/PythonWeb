import json
from models import Author, Quote
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import certifi
from mongoengine import connect, disconnect

uri = "mongodb+srv://vikki1993123:Vikki123%40@cluster0.oricvyp.mongodb.net/testdb?retryWrites=true&w=majority"

# Establish a connection to MongoDB
connect(db='testdb', alias='default', host=uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

# Insert authors data
with open('authors.json', 'r', encoding='utf-8') as file:
    authors_data = json.load(file)
    for author_data in authors_data:
        author_instance = Author(**author_data)
        author_instance.save()

# Insert quotes data
with open('quotes.json', 'r', encoding='utf-8') as file:
    quotes_data = json.load(file)
    for quote_data in quotes_data:
        quote_instance = Quote(**quote_data)
        quote_instance.save()

print('Data insertion completed successfully.')

# Disconnect from MongoDB when done
disconnect()
