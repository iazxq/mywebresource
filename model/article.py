# -*- coding: utf-8 -*-
import sys
sys.path.append("d:\python\sharejs")
import datetime
from common import func

class Article:

    def __init__(self,data=None):
        if data:
            self.load_from_data(data)
        else:
            self.id = 0
            self.root_category_id = 0
            self.category_id = 0
            self.category_id2 = 0
            self.category_id3 = 0
            self.title = ''
            self.author =''
            self.source = ''
            self.short_description = ''
            self.description = ''
            self.demo_code =''
            self.demo_url = ''
            self.dev_view_code = ''
            self.full_download_url = ''
            self.head_code = ''
            self.body_code =''
            self.compatibility = ''
            self.pic = ''
            self.small_pic = ''
            self.topic_id = 0
            self.state =0
            self.isrtdate = datetime.datetime.now()
            self.hits = 0
            self.download = 0
            self.recommend = 0
            self.last_hit_date = datetime.datetime.now()

    def load_from_data(self,data):
        self.id = data.get('id',0)
        self.root_category_id = data.get('root_category_id',0)
        self.category_id = data.get('category_id',0)
        self.category_id2 = data.get('category_id2',0)
        self.category_id3 = data.get('category_id3',0)
        self.title = data.get('title','')
        self.author = data.get('author','')
        self.source = data.get('source','')
        self.short_description = data.get('short_description','')
        self.description = data.get('description','')
        self.demo_code = data.get('demo_code','')
        self.demo_url = data.get('demo_url','')
        self.dev_view_code = data.get('dev_view_code','')
        self.full_download_url = data.get('full_download_url','')
        self.head_code = data.get('head_code','')
        self.body_code = data.get('body_code','')
        self.compatibility = data.get('compatibility','')
        self.pic = data.get('pic','')
        self.small_pic = data.get('small_pic','')
        self.topic_id = data.get('topic_id',0)
        self.state = data.get('state',0)
        self.isrtdate = func.str_to_datetime(data.get('isrtdate',str(datetime.datetime.now())))
        self.hits = data.get('hits',0)
        self.download = data.get('download',0)
        self.recommend = data.get('recommend',0)
        self.last_hit_date = func.str_to_datetime(data.get('last_hit_date',str(datetime.datetime.now())))

    def get_json(self):
        return {
        'id':self.id,
        'root_category_id':self.root_category_id,
        'category_id':self.category_id,
        'category_id2':self.category_id2,
        'category_id3':self.category_id3,
        'title':self.title,
        'author' : self.author,
        'source':self.source ,
        'short_description':self.short_description ,
        'description':self.description ,
        'demo_code':self.demo_code ,
        'demo_url':self.demo_url ,
        'dev_view_code':self.dev_view_code,
        'full_download_url':self.full_download_url,
        'head_code':self.head_code ,
        'body_code':self.body_code ,
        'compatibility':self.compatibility ,
        'pic':self.pic ,
        'small_pic':self.small_pic ,
        'topic_id':self.topic_id ,
        'state':self.state,
        'isrtdate':func.format_date_time(self.isrtdate) ,
        'hits':self.hits,
        'download':self.download ,
        'recommend':self.recommend,
        'last_hit_date':func.format_date_time(self.last_hit_date),
        }



if __name__ == "__main__":
    article = Article()
    article.id = 1234;
    article.isrtdate = datetime.datetime.now()
    print(article.__dict__)