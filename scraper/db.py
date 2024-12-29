from pymongo import MongoClient


class Database:
    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client["scraper"]
        self.collection = self.db["news"]

    def insert(self, data):

        trends = data["trends"]

        new_data = {
            "nameoftrend1": trends[0],
            "nameoftrend2": trends[1],
            "nameoftrend3": trends[2],
            "nameoftrend4": trends[3],
            "nameoftrend5": trends[4],
            "date": data["date"],
            "time": data["time"],
        }

        return self.collection.insert_one(new_data)

    def find_one(self, query={}):
        return self.collection.find_one(query)

    def delete(self, query):
        self.collection.delete_many(query)

    def close(self):
        self.client.close()


db = Database()
