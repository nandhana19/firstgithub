from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def dhoni (request):
    return HttpResponse ('<h1>dhoni scores century</h1>') 

    