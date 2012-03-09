# -*- coding: utf-8 -*-
import sys
sys.path.append("d:\python\sharejs")

from mysqldb import DB
from model.taghot import TagHot

class TagHotRepository(DB):
    def __init__(self):
        DB.__init__(self)


    def get_data(self,tag):
        self.cursor.execute('select * from taghot where tag=%(tag)s',{'tag':tag})
        result = self.cursor.fetchone()
        if result:
            return TagHot(result)
        else:
            return None


    def insert(self,tag,hot):
        self.cursor.execute('insert into taghot (tag,hot)values(%(tag)s,%(hot)s)',{'tag':tag,'hot':hot})
        self.cursor.connection.commit()

    def update(self,tag,hot=0):
        self.cursor.execute('update taghot set hot=%(hot)s where tag=%(tag)s',{'tag':tag,'hot':hot})
        self.cursor.connection.commit()

    def get_hot_list(self,count=10):
        self.cursor.execute('select * from taghot order by hot desc limit %(count)s',{'count':count})
        result = map(lambda row: TagHot(row), self.cursor.fetchall())
        return result


if __name__== "__main__":
    pass
