from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def captain (request):
    return HttpResponse ('<h1>last year kkr won the match</h1>') 
