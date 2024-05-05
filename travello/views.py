from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):
    # return HttpResponse("Hello World")#we can write h1 or any tags but it is not good approach for making website dynamic

    dests = Destination.objects.all()
    
    return render(request,'index.html',{'dests' : dests})
