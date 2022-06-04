from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from .views import shorten_the_long_url,redirect_to_long_url


urlpatterns = [

    url(r'^$',shorten_the_long_url),
    url(r'^(?P<hash_value>\w+)',redirect_to_long_url),
#    url(r'^')

]
