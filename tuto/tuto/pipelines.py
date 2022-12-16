from itemadapter import ItemAdapter
import pymongo


class MongoMovies:

    def __init__(self):
        client = pymongo.MongoClient(
            'mongodb+srv://zoltar:"+gargaMEL80!+"@zoltar.dbytmfn.mongodb.net/?retryWrites=true&w=majority'
        )

        db = client['IMDB']
        collection = db['Movies']

    def process_item(self, item, collection):
        collection.insert_one(dict(item))
        return item