# -*- coding: utf-8 -*-
import sys
sys.path.append("d:\python\sharejs")
import datetime


class ArticleJS:

    def __init__(self,data=None):
        self.load_from_data(data)


    def load_from_data(self,data):
        if data:
            self.demo_code = js_data.get('demo_code','')
            self.demo_url = js_data.get('demo_url','')
            self.dev_view_code = js_data.get('dev_view_code','')
            self.head_code = js_data.get('head_code','')
            self.body_code = js_data.get('body_code','')

    def get_json(self):
        return self.__dict__



if __name__ == "__main__":
    article = ArticleJS()
    article.id = 1234;
    article.isrtdate = datetime.datetime.now()
    print(article.__dict__)