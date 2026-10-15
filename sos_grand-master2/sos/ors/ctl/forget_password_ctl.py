from django.shortcuts import render, redirect

from ..ctl.base_ctl import BaseCtl
from ..utility.data_validator import DataValidator
from ..service.forget_password_service import ForgetPasswordService

class ForgetPasswordCtl(BaseCtl):

    def request_to_form(self, request):
        self.form['login_id'] = request.POST.get('loginId')

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False

        if (DataValidator.is_null(request.POST.get("loginId", ''))):
            input_error['login_id'] = 'Login ID is required'
            input_error['error'] = True
        return input_error['error']

    def display(self, request, params={}):
        return render(request,self.get_template(),{'form': self.form})

    def submit(self, request, params={}):
        user_list = self.get_service().find_by_login(self.form['login_id'])
        user = user_list.first()

        if user is not None:
            self.form['message'] = ('your password is: '+str(user.password))
            self.form['error'] = False

        else:
            self.form['message'] = 'Login ID  does not exit'
            self.form['error'] = True

        return self.display(request)



    def get_template(self):
        return "forget_password.html"

    def get_service(self):
        return ForgetPasswordService()