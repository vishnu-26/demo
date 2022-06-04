import os
from db_connection import connect
from dotenv import load_dotenv
from bson.json_util import dumps, loads

load_dotenv()

# Create your models here.

class User:
    def __init__(self, user_id, **kwargs):
        self.db = connect()
        self.collection = self.db['user']
        self.user_id = user_id
        self.attributes = kwargs


    def create(self):
        
        user_document = {
            "user_id": self.user_id,
            "password": self.attributes.get("password",""),
            "name": self.attributes.get("name",""),
            "address": self.attributes.get("address","")
        }

        self.collection.insert_one(user_document)


    def find(self):
        user = self.collection.find_one({"user_id": self.user_id})
        user.pop('_id')
        return user
        '''Converting user dict to json serializable'''
#        return loads(dumps(user))
        



