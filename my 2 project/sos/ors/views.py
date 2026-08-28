from django.http import HttpResponse
from django.shortcuts import render


def testors(request):
    return HttpResponse('<h1>this is ors app</h1>')

def display(request):
    return HttpResponse('<h1> this is display</h1>')

def welcome(request):
    return render (request,'welcome.html')