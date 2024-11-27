from django.urls import path
from kkr.views import *
urlpatterns=[
    path('captain/',captain,name='captain'),
]