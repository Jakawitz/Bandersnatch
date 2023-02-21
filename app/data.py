from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient
import random


class Database:
    load_dotenv()
    database = MongoClient(getenv("DB_URL"), tlsCAFile=where())["demodb"]

    def __init__(self, database=database):
        self.collection = database["test"]

    def seed(self, amount):
        # fill with mock data
        doc_list = []
        while amount > 0:
            man = Monster()
            doc_list.append(man.to_dict())
            amount -= 1
        self.collection.insert_many(doc_list)

    def reset(self):
        # mass delete mock data
        self.collection.delete_many({})

    def count(self) -> int:
        # count records(rows) in a collection(table)
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        # return group of records as a DataFrame
        curs = self.collection.find({}, {"_id": 0})
        df = DataFrame(list(curs))
        return df

    def html_table(self) -> str:
        # transferring DataFrame to an html_table
        df = self.dataframe()
        return df.to_html()


if __name__ == '__main__':
    db = Database()
    db.reset()
    db.seed(amount=1000)
