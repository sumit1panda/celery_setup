from django.shortcuts import render,HttpResponse,redirect
from .task import *
# Create your views here.
def index(request):
    #sleepy.delay(10)
    res=cal.delay()
    print (res)
    return HttpResponse('It is working!!')