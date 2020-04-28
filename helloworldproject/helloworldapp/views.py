from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hellofunction(reques):
    return HttpResponse('hello world')