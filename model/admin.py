# -*- coding: utf-8 -*-

class Admin:

    def __init__(self,data):
        if data:
            self.load_from_data(data)

    def format_data(self):
        return {
            'username':self.username,
            'password':self.password,
            'grade':self.grade,
        }

    def load_from_data(self,data):
        self.username = data.get('username','')
        self.password = data.get('password','')
        self.grade = data.get('grade',0)