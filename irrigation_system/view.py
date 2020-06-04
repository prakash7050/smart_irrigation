from django.http import HttpResponse
from django.shortcuts import render
from projects.models import projects




def home(request):
    return render(request , 'h1.html' , {'key1' : 'Iam coming from python code'})

def result(request):
    age = request.GET['user_age']
    name = request.GET['user_name']
    message = f'Hi,{name},you are {age} years old'
    return render(request,'result.html',{'age':message})

def test(request):
    project = projects.objects
    return render(request , 'test.html',{'projects':project})