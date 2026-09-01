from django.http import HttpResponse
from django.shortcuts import render


def test_ors(request):
    return HttpResponse('<h1> this is ors app</h1>')

def welcome(request):
    return render(request,'welcome.html')

def user_signup(request):
    return render(request,'registration.html')

def user_sigin(request):
    return render(request,'login.html')