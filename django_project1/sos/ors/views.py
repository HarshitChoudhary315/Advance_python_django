from django.http import HttpResponse
from django.shortcuts import render, redirect

from .service.user_service import UserService


def test_ors(request):
    return HttpResponse('<h1> this is ors app</h1>')

def welcome(request):
    return render(request,'welcome.html')

def user_signup(request):
    if request.method == "POST":
     form = {}
     form['first_name'] = request.POST.get('firstName')
     form['last_name'] = request.POST.get('lastName')
     form['login_id'] = request.POST.get('loginId')
     form['password'] = request.POST.get('password')
     form['dob'] = request.POST.get('dob')
     form['address'] = request.POST.get('address')

     service = UserService()
     service.add(form)
    return render(request,'registration.html')

def user_sigin(request):
    message = ''
    if request.method =="POST":
        form = {}
        form['login_id'] = request.POST.get('loginId')
        form['password'] = request.POST.get('password')
        service = UserService()
        records = service.authenticate( form['login_id'],form['password'])

        if len(records) > 0:
            request.session['first_name'] = records[0].get('first_name')
            return render(request,'welcome.html',{'firstName': records[0].get('first_name')})
        else:
            message = 'login & password Invalid'

    return render(request,'login.html',{'message':message})

def user_logout(request):
    request.session['first_name'] = None
    return redirect('/ors/signin/')



def test_list(request):
    list = [
        {"id":1,"first_name":"Rahul","last_name":"Sharma","email":"rahul@gmail.com","password":"rahul123"},
        {"id":2,"first_name": "Pryia","last_name": "Verma","email":"pryia@gmail.com","password":"pryia123"},
        {"id":3,"first_name": "Amit","last_name": "Patel","email":"amit@gmail.com","password":"amit123"},
        {"id":4,"first_name": "Neha","last_name": "Singh","email":"neha@gmail.com","password":"neha123"},
        {"id":5,"first_name": "Rohit","last_name": "Gupta","email":"rohit@gmail.com","password":"rohit123"}
    ]
    return render(request,'test_list.html',{'list':list})

def user_list(request):
    form = {}
    form['page_no'] = 1
    form['page_size'] = 5

    service = UserService()
    list = service.search(form)
    return render(request,'user_list.html',{'list':list})
