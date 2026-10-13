from django.shortcuts import render

from .base_ctl import BaseCtl
from ..service.user_service import UserService
from ..utility.html_utility import HtmlUtility
from ..service.role_service import RoleService

class TestCtl(BaseCtl):
    def preload(self, request):
        gender_list = ["Male", "Female"]
        role_list = RoleService().search({})
        user_list = UserService().search({})

        self.form["preload_data"]["gender_select"] = HtmlUtility.get_list_from_list(
            "gender",
            self.form.get("gender"),
            gender_list
        )

        self.form["preload_data"]["role_select"] = HtmlUtility.get_list_from_beans(
            "roleId",
            int(self.form.get("role_id") or 0),
            role_list
        )
        self.form["preload_data"]["user_select"] = HtmlUtility.get_list_from_beans(
            "userId",
            int(self.form.get("user_id") or 0),
            user_list
        )

    def request_to_form(self, request):
        self.form['gender'] = request.POST.get('gender', '')
        self.form['role_id'] = request.POST.get('roleId', '')
        self.form['user_id'] = request.POST.get('userId', '')


    def display(self,request,params={}):
        return render(request, 'test.html', {'form': self.form,  "preload_data": self.preload(request)})

    def submit(self,request,params={}):
        if request.POST.get('operation', '') == "signIn":
            return render(request,'test.html',{'form': self.form,  "preload_data": self.preload(request)})




