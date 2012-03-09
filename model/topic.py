# -*- coding: utf-8 -*-

class Topic:
    def __init__(self,data):
        self.load_from_data(data)

    def load_from_data(self,data):
        self.topic_id = data.get('topic_id',0)
        self.title = data.get('title','')
        self.pic = data.get('pic','')
        