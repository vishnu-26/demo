import jwt
import datetime
from django.conf import settings
from .models import User

def generate_token(user):
    payload={
        'user_id': user['user_id'],
        'exp': datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
#        'jwt':datetime.datetime.utcnow()
    }

    return jwt.encode(payload,settings.SECRET_KEY,'HS256')


def is_authenticated(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION').split()[1]

        if not token:
            user = None
            
        payload=jwt.decode(token,settings.SECRET_KEY,'HS256')
        user = User(payload['user_id'])
        user = user.find()
    except:
        user = None
        
#        kwargs['user']= user
#        print(kwargs) 
    return user
