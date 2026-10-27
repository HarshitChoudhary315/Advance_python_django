from ..service.base_service import BaseService
from ..dao.student_dao import StudentDAO



class StudentService(BaseService):

    def get_dao(self):
        return StudentDAO()