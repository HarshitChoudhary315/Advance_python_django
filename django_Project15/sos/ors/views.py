from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def test_ors(request):
    return HttpResponse('<h1> this is ors app of project 15</h1>')

def welcome(request):
    return render(request,'welcome.html')

def user_signup(request):
    if request.method == "POST":
        print(request.POST.get('firstName'))
        print(request.POST.get('lastName'))
        print(request.POST.get('loginId'))
        print(request.POST.get('password'))
        print(request.POST.get('dob'))
        print(request.POST.get('address'))

    return render(request,'registration.html')

def user_signin(request):
    if request.method == "POST":
     print(request.POST.get('loginId'))
     print(request.POST.get('password'))
    return render(request,'login.html')