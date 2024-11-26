from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def venkatesh(request):
    return HttpResponse ('<h1>venkatesh is captain of KKR</h1>') 

