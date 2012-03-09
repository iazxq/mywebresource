# -*- coding: utf-8 -*-
'''
  article相关的redis操作库
'''


from redis_db import RedisDB
from model.article import  Article
from repository.articlerepository import ArticleRepository
import json

class ArticleRedis(RedisDB):
    def __init__(self):
        RedisDB.__init__(self)

    def get_data(self,id):
        result = self.redis.get('subject:%s'%id)
        if result:
            result = eval(result)
            article = Article()
            article.load_from_data(result)
            return article
        else:
            return None

    def set_data(self,id,article,time=0):
        '''
        存详细信息到redis，默认有效时间为1小时
        '''
        key = 'subject:%s'%id
        if time>0:
            self.redis.setex(key,article.get_json(),time)
        else:
            self.redis.set(key,article.get_json())

    def delete(self,id):
        return self.redis.delete('subject:%s'%id)





if __name__== "__main__":
    '''article_repository = ArticleRepository()
    article = article_repository.get_data(3233)
    r = ArticleRedis()
    r.set_data(3233,article,0)
    a = r.get_data(3233)
    print(a.title)'''

    r = ArticleRedis()
    print(r.get_data(1))