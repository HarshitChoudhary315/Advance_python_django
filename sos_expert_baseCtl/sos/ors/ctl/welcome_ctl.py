from django.shortcuts import render

from ..ctl.base_ctl import BaseCtl


class WelcomeCtl(BaseCtl):

    def display(self,request,parmas={}):
        return render(request,'welcome.html')

    def submit(self,request,parmas={}):
        return render(request,'welcome.html')