from django.shortcuts import render
from . HTML_STRINGS import *                # will hold a set of strings that will be used as html
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return HttpResponse(HomePage)