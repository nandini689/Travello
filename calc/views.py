from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# you are requesting for the response 


def home(request):
    # return HttpResponse("Hello World")#we can write h1 or any tags but it is not good approach for making website dynamic
    return render(request,'home.html',{'name':'Nandini'})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request,'result.html',{'result':res})
