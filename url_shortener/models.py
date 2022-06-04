import os
import base62
import pymongo
import threading
from db_connection import connect
#from .utils import generate_short_code
from dotenv import load_dotenv

load_dotenv()

import logging
logger = logging.getLogger(__name__)

class Url:
    def __init__(self,link, hash_value, **kwargs):
        self.db = connect()
        self.collection = self.db['url']
        self.link = link
        self.hash = hash_value
        self.attributes = kwargs


    def create(self):
#        url = self.collection.find_one({'long':self.long})
#        print(cursor)
#        
#        if url:
#            url=list(cursor)
#            print(url)
#            self.short = url['short']
#            return
        
#        self.short = self.generate_short()
#        logger.debug(f'Gerated hash_value : {self.short} for url: {self.long}')

        url_document = {
            'link': self.link,
            'hash': self.hash,
        }
        for key in self.attributes.keys():
            url_document[key] = self.attributes.get(key)

        logger.debug(f'url_document created: {url_document}')
        try:
            self.collection.create_index([('hash',pymongo.TEXT)])
#            self.collection.ensure_index('expires_at',expireAfterSeconds= 0)
            try:
                threading.Thread(target= self.collection.insert_one(url_document)).start()
            except:
                logger.exception(f'Error while inserting url {self.link}')
        except:
            logger.exception('Error while creating index')

        
        return
         
        
    
    def get_link(self):
        url = self.collection.find_one({'hash': self.hash})
        if url:
            logger.info(f'Found the long url/link for hash: {self.hash} in db')
            return url
#            self.link = url['link']
#            self.attributes = {'expires_at': url['expires_at']}


    def inc_link_redirections(self):
        self.collection.update({'hash': self.hash},{"$inc": {"no_of_redirections": 1}})


#    def generate_short(self):
#        short_code = generate_short_code(){"num": 41}
#        url = self.collection.find_one({'short': short_code})
#
#        if url:
#            url = list(cursor)
#            return self.generate_short()
#        return short_code
#
    def is_hash_present(self):
        return self.collection.find_one({'hash': self.hash})

        

            
