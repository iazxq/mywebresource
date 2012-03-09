# -*- coding: utf-8 -*-

class TagHot:

    def __init__(self,data=None):
        if data:
            self.load_from_data(data)
            return


    def format_data(self):
        return {
            'id':self.id,
            'tag':self.tag,
            'hot':self.hot,
        }

    def load_from_data(self,data):
        self.id = data.get('id',0)
        self.hot = data.get('hot',0)
        self.tag = data.get('tag','')