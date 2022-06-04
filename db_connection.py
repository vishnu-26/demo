import pymongo
import os
from dotenv import load_dotenv

load_dotenv()

def connect(db_name="url_shortener"):
    try:
        client = pymongo.MongoClient(os.getenv('MONGODB_URI'))
        db = client[db_name]
        print('Mongodb Connected: ',db)
        
    except:
        db =None
    
    return db
    


if __name__=='__main__':
    connect()
