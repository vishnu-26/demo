import json
import time
import os
import threading
from django.shortcuts import render,redirect
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Url
from redis_connection import redis_connect
import datetime
from .utils import generate_hash
from user.authentication import is_authenticated

from .throttling import CustomRateThrottling

from dotenv import load_dotenv
load_dotenv()

import logging
logger = logging.getLogger(__name__)

@api_view(['POST'])
@throttle_classes([CustomRateThrottling])
def shorten_the_long_url(request):
    link = request.data['url']

    hash_value= generate_hash()
    created_at = datetime.datetime.utcnow()

    user = is_authenticated(request)

    if user:
        user_id = user.get('user_id')
        u = Url(link, hash_value, **{'user_id':user_id, 'created_at':created_at})

    else:
        u = Url(link, hash_value, **{'created_at':created_at})


    u.create()
    return Response({
        'short_url': os.getenv('DOMAIN_NAME') + u.hash
    },status=201)
#    else:
#        return Response({
#            'Error': 'Something went worng!!, Please try again'
#        },status=500)




@api_view(['GET'])
def redirect_to_long_url(request,hash_value=None):

    u = Url(None,hash_value)
    re = redis_connect()

    if re.exists(hash_value):
        link = re.get(hash_value)

        '''Increment no of redirections concurrently'''
        threading.Thread(target= u.inc_link_redirections())

        return redirect(link)
    else:
        url = u.get_link()
        if url is None:
            return JsonResponse({'msg': 'Error! Bad Request'},status= 400)

        '''Insert into redis'''
        re.set(
            url.get('hash'),
            url.get('link')
        )


        '''Increment no of redirections concurrently'''
        threading.Thread(target= u.inc_link_redirections())

        return redirect(url.get('link'))
