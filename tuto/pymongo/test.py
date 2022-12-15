import pymongo
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
PASSWORD = os.getenv('PASSWORD')

#connect to the MongoDB
client = pymongo.MongoClient("mongodb+srv://zoltar:"+PASSWORD+"@zoltar.dbytmfn.mongodb.net/?retryWrites=true&w=majority")

#Create a Database
db = client['sample_db']

#Create a Collection
collection = db['sample_collection']

#Insert a Document
sample_document = {
    'name': 'John Doe', 
    'age': 21, 
    'location': 'New York'
}
collection.insert_one(sample_document)

#Query a Document
query_result = collection.find_one({'name': 'John Doe'})
if query_result:
    print('Document found!')
    print(query_result)
else:
    print('No document found!')

#Update a Document
update_result = collection.update_one({'name': 'John Doe'}, {'$set': {'age': 24}})
if update_result.modified_count > 0:
    print('Document updated!')
else:
    print('No document updated!')

#Delete a Document
delete_result = collection