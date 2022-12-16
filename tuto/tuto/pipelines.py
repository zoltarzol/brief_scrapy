import pymongo
from dotenv import load_dotenv
import os

load_dotenv()

PASSWORD = os.getenv('PASSWORD')

class MongoMovies:

    def __init__(self):
        client = pymongo.MongoClient(
            'mongodb+srv://zoltar:'+PASSWORD+'@zoltar.dbytmfn.mongodb.net/?retryWrites=true&w=majority'
        )

        db = client['IMDB']
        self.collection = db['Movies']
        self.collection.drop()

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item