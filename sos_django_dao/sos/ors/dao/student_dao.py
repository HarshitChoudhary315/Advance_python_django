from .base_dao import BaseDAO
from ..models import Student
from ..utility.data_validator import DataValidator


class StudentDAO(BaseDAO):

    def get_unique_key(self):
        return "email"

    def get_model(self):
        return Student

    def get_label(self):
        return "email"

    def get_where_clause(self, query, params):
        value = params.get("name","")

        if DataValidator.is_not_null(value):
            query = query.filter(email__isstartwith=value.strip())

        return query