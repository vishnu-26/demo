from rest_framework.decorators import api_view
from django.http import JsonResponse
from .authentication import generate_token
from .authentication import is_authenticated

from .models import User

# Create your views here.

@api_view(['POST'])
def register(request):
    user_id = request.data.get("user_id")
    password  = request.data.get("password")
    name = request.data.get("name")
    address= request.data.get("address")

#    if data['password'] != data['confirm_password']:
#        return JsonResponse({ 'msg': 'Error! Password and Confirm Password do not match'},status=400)

    # hashed_password=bcrypt.hashpw(data['password'].encode("utf-8"),bcrypt.gensalt())
    # data['password']=hashed_password



    user = User(user_id, **{"password":password,"name":name,"address":address})
    user.create()

#        return JsonResponse({'msg': 'Some error occurred!! Please try again.'},status= 500)
#
    return JsonResponse(
        {'msg': 'Registered Successfully'},status=201)


@api_view(['POST'])
def login(request):
    user_id=request.data.get("user_id")
    password = request.data.get("password")


    user = User(user_id)
    user = user.find()

    if not user:
        return JsonResponse({'msg':'User Id does not exist'},status=400)

    if password != user.get("password"):
        return JsonResponse({'msg': 'Inavlid Password'},status=400)

    token = generate_token(user)

    return JsonResponse(
        {"user": user,"token": token,'message':'Login Success!!'},status= 200)
        


@api_view(['POST'])
def authenticate(request):
    user = is_authenticated(request)

    if user:
        return JsonResponse({'msg':'Success!!','user':user},status=200)
    else:
        return JsonResponse({'msg':'Error!!'},status=200)
