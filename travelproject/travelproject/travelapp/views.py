from django.shortcuts import render
from django.http import HttpResponse
from. models import time



# Create your views here.
def demo(request):
    obj=time.objects.all()
    return render(request,"index.html",{'result':obj})


