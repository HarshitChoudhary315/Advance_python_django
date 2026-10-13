from django.shortcuts import render

from .base_ctl import BaseCtl
from ..models import Marksheet
from ..service.marksheet_service import MarksheetService
from ..utility.data_validator import DataValidator


class MarksheetCtl(BaseCtl):

    def input_validation(self, request):
        input_error = self.form.get("input_error")
        input_error['error'] = False
        if (DataValidator.is_null(request.POST.get("roll_number", ''))):
            input_error['roll_number'] = 'roll_number is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("name", ''))):
            input_error['name'] = 'name is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("physics", ''))):
            input_error['physics'] = 'physics is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("chemistry", ''))):
            input_error['chemistry'] = 'chemistry is required'
            input_error['error'] = True
        if (DataValidator.is_null(request.POST.get("maths", ''))):
            input_error['maths'] = 'maths is required'
            input_error['error'] = True
        return input_error['error']

    def request_to_form(self, request):
        self.form['id'] = int(request.POST.get('id') or 0)
        self.form['roll_number'] = request.POST.get('roll_number', '')
        self.form['name'] = request.POST.get('name', '')
        self.form['physics'] = request.POST.get('physics', '')
        self.form['chemistry'] = request.POST.get('chemistry', '')
        self.form['maths'] = request.POST.get('maths', '')

    def form_to_model(self, obj):
        obj.id = self.form['id']
        obj.roll_number = self.form['roll_number']
        obj.name = self.form['name']
        obj.physics = self.form['physics']
        obj.chemistry = self.form['chemistry']
        obj.maths = self.form['maths']
        return obj

    def model_to_form(self, obj):
        self.form['id'] = obj.id
        self.form['roll_number'] = obj.roll_number
        self.form['name'] = obj.name
        self.form['physics'] = obj.physics
        self.form['chemistry'] = obj.chemistry
        self.form['maths'] = obj.maths

    def display(self, request, params = {}):
        return render(request, self.get_template(), {'form': self.form})

    def submit(self, request,params = {}):
            try:
                marksheet = self.form_to_model(Marksheet())
                self.get_service().save(marksheet)
                if self.form['id'] > 0:
                    self.form['message'] = 'marksheet update Successfully...!!!'
                    self.form['error'] = False
                else:
                    self.form['message'] = 'marksheet saved successfully...!!!'
                    self.form['error'] = False

            except Exception as e:
                self.form['message'] = str(e)
                self.form['error'] = True

            return render(request,self.get_template(), {'form': self.form})

    def get_service(self):
        return MarksheetService()

    def get_template(self):
        return 'marksheet.html'