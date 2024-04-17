from django.shortcuts import render
from .models import Place,Member

# Create your views here.
def myfun(request):
    obj = Place.objects.all()
    return render(request,'index.html',{'result':obj})

def mymember(request):
    obj = Member.objects.all()
    return render(request,'index.html',{'members':obj})