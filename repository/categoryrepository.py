# -*- coding: utf-8 -*-
import sys
sys.path.append("d:\python\sharejs")

from mysqldb import DB
from model.category import Category

class CategoryRepository(DB):
    def __init__(self):
        DB.__init__(self)


    def get_data(self,category_id):
        self.cursor.execute('select * from category where category_id=%(category_id)s',{'category_id':category_id})
        category_dict = self.cursor.fetchone()
        if category_dict:
            return Category(category_dict)
        else:
            return None

    def get_child_category_list(self,category_id):
        self.cursor.execute('select * from category where parent_category_id=%(parent_category_id)s',{'parent_category_id':category_id})
        category_dict_list = self.cursor.fetchall()
        return map(lambda category_dict:Category(category_dict),category_dict_list)

    def insert(self,category):
        self.cursor.execute('insert into category(category_id,parent_category_id,root_category_id,category_name)values(%(category_id)s,%(parent_category_id)s,%(root_category_id)s,%(category_name)s)',category.__dict__)
        self.cursor.connection.commit()

    def remove(self,category_id):
        self.cursor.execute('delete from category where category_id=%(category_id)s',{'category_id':category_id})
        self.cursor.connection.commit()

    def update(self,category):
        self.cursor.execute('''
                            update category set
                            parent_category_id=%(parent_category_id)s,
                            root_category_id=%(root_category_id)s,
                            category_name=%(category_name)s,
                            article_type=%(article_type)s,
                            description=%(description)s
                            where category_id=%(category_id)s
                            ''',category.__dict__)
        self.cursor.connection.commit()


if __name__== "__main__":
    category_repository = CategoryRepository()
    print(category_repository.get_child_category_list(100))
