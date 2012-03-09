# -*- coding: utf-8 -*-

class Tag:

    def __init__(self,data=None,article_id=None,tag=None):
        if data:
            self.load_from_data(data)
            return

        if article_id and tag :
            self.article_id = article_id
            self.tag = tag



    def format_data(self):
        return {
            'id':self.id,
            'article_id':self.article_id,
            'tag':self.tag,
        }

    def load_from_data(self,data):
        self.id = data.get('id',0)
        self.article_id = data.get('article_id',0)
        self.tag = data.get('tag','')