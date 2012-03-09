# -*- coding: utf-8 -*-

from mysqldb import DB


class AdminRepository(DB):

    def __init__(self):
        DB.__init__(self)

    def add_new_admin(self,admin):
        '添加新的管理员'
        pass
        #self.cursor.execute('insert into admin(username,password,intro)values(:username,:password,:intro)',admin)

    def login(self,username,password):
        self.cursor.execute('select * from admin where username=%(username)s and password=%(password)s',{'username':username,'password':password})
        data = self.cursor.fetchone()
        if data:
            return True
        else:
            return False