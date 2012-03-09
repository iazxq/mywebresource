# -*- coding: utf-8 -*-

class Category:

    def __init__(self,data=None):
        if data:
            self.load_from_data(data)

    def load_from_data(self,data):
        self.category_id = data.get('category_id',0)
        self.category_name = data.get('category_name','')
        self.parent_category_id = data.get('parent_category_id',0)
        self.root_category_id = data.get('root_category_id',0)
        self.article_type = data.get('article_type',0)
        self.description = data.get('description','')

    def get_json(self):
        return {
            'category_id':self.category_id,
            'category_name':self.category_name,
            'parent_category_id':self.parent_category_id,
            'root_category_id':self.root_category_id,
            'article_type':self.article_type,
            'description':self.description,
        }

    def format_data(self):
        return {
            'category_id':self.category_id,
            'category_name':self.category_name,
            'parent_category_id':self.parent_category_id,
            'root_category_id':self.root_category_id,
            'article_type':self.article_type,
            'description':self.description,
        }

    def __repr__(self):
        return repr(self.format_data())


if __name__=='__main__':
    category = Category()
    category.category_id = 1
    print(category.__dict__)