# -*- coding: utf-8 -*-

from repository.admin import AdminRepository

class AdminFacade:
    '管理员管理'
    def __init__(self):
        pass


    def login(self,username,password):
        admin_repository = AdminRepository()
        with admin_repository:
            return admin_repository.login(username,password)