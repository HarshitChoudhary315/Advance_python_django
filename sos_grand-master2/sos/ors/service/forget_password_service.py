from ..models import User
from ..utility.data_validator import DataValidator


class ForgetPasswordService:
    def find_by_login(self, login_id):

        print('user service orm find_by_login()')
        obj = User.objects.filter(login_id=login_id)
        return obj


    def get_model(self):
        return User