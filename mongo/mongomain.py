from pymongo import MongoClient
import json


with open("configuration.json", "r") as config: 
    data = json.load(config)
    url = data["mongourl"]


def get_database():

    connect = url

    client = MongoClient(connect)

    return client['receita']

if __name__=="__main__":
    minhadb = get_database()