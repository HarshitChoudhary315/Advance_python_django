from django.db import connection


class UserService:

    def next_pk(self):
        pk = 0
        cursor = connection.cursor()
        sql = "select max(id) from sos_user"
        cursor.execute(sql)
        result = cursor.fetchall()
        for data in result:
            if data[0] is not None:
                pk = data[0]
        connection.commit()
        connection.close()
        return pk + 1

    def add(self, data):
        id = UserService.next_pk(self)
        first_name = data['first_name']
        last_name = data['last_name']
        login_id = data['login_id']
        password = data['password']
        dob = data['dob']
        address = data['address']

        cursor = connection.cursor()
        sql = "insert into sos_user values(%s, %s, %s, %s, %s, %s, %s)"
        data = (id, first_name, last_name, login_id, password, dob, address)
        cursor.execute(sql, data)
        connection.commit()
        connection.close()
        print("data inserted successfully")
