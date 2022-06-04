import time
import json
from locust import HttpUser, task, between
from url_shortener.models import Url
from redis_connection import redis_connect


class QuickstartUser(HttpUser):
#    wait_time = between(1, 5)

    def on_start(self):
        self.long = 'https://whimsical.com/dbms-roadmap-by-love-babbar-FmUi8ffVop33t3MmpVxPCo'
        self.short=None
#        print("Hello!!")

    @task
    def short_url(self):
        resp = self.client.post('',json={'url':self.long}).content
        resp = json.loads(resp.decode('utf-8'))
        print(resp)
        self.short = resp['short_url']
#        print(type(self.short))
        

#    @task
#    def get_long_url(self):
#        self.client.get(self.short)
        

        
