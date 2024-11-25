from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def nandhanaa (request):
    return HttpResponse('my name is nandhana')
    
def harisha (request):
    return HttpResponse('harisha is a innocent girl')  
def saddam (request):
    return HttpResponse('saddam') 
def django (request):
    return HttpResponse('django')   
          
def python (request):
    return HttpResponse('<h1><marquee>programming language</marquee></h1>')          
def python (request):
    return HttpResponse('<h1><img srcprogramming language</marquee></h1>')          