# -*- coding: utf-8 -*-

import sqlite3
import pymysql
import settings

class DB:
    def __init__(self):
        try:
            def dict_factory(cursor, row):
                d = {}
                for idx,col in enumerate(cursor.description):
                    d[col[0].lower()] = row[idx]
                return d
            sqlite3.paramstyle = 'pyformat'
            self.connection = sqlite3.Connection(settings.DATABASES['default']['NAME'])
            self.connection.row_factory = dict_factory
        except():
            exit(1)
        self.cursor = self.connection.cursor()


    def dispose(self):
        pass


    def __enter__(self):
        return self

    def  __exit__(self, type, value, traceback):
        self.dispose()


class MySqlDB:
    def __init__(self):
        try:
            self.connection = pymysql.connect(host='127.0.0.1', db='sharejs',user='root', passwd='',charset='utf8')
        except():
            exit(1)
        self.cursor = self.connection.cursor()


    def dispose(self):
        pass


    def __enter__(self):
        return self

    def  __exit__(self, type, value, traceback):
        self.dispose()