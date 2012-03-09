# -*- coding: utf-8 -*-

import pymysql
import pymysql.cursors
import settings

class DB:
    def __init__(self):
        try:
            self.connection = pymysql.connect(host='127.0.0.1', db='js',user='root', passwd='',charset='utf8')
        except():
            exit(1)
        self.cursor = self.connection.cursor(cursor=pymysql.cursors.DictCursor)



    def dispose(self):
        pass


    def __enter__(self):
        return self

    def  __exit__(self, type, value, traceback):
        self.dispose()