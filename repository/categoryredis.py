# -*- coding: utf-8 -*-
'''
  category相关的redis操作库
'''


from redis_db import RedisDB
from model.category import  Category
from repository.categoryrepository import CategoryRepository
import json

class CategoryRedis(RedisDB):
    def __init__(self):
        RedisDB.__init__(self)

    def get_data(self,id):
        result = self.redis.get('cat:%s'%id)
        if result:
            result = eval(result)
            category=Category()
            category.load_from_data(result)
            return category
        else:
            return None

    def set_data(self,category,time=0):
        '''
        存详细信息到redis，默认有效时间为无限长
        '''
        if category:
            key = 'cat:%s'%category.category_id
            if time>0:
                self.redis.setex(key,category.get_json(),time)
            else:
                self.redis.set(key,category.get_json())

    #从缓存获取子分类列表
    def get_child_category_list(self,category_id):
        category_list = list()
        result = self.redis.get('child_cat_list:%s'%category_id)
        if result:
            result = eval(result)
            for item in result:
                category = Category()
                category.load_from_data(item)
                category_list.append(category)
        return category_list

    #设置子分类列表到缓存
    def set_child_category_list(self,category_id,category_list):
        result = []
        for category in category_list:
            result.append(category.get_json())
        self.redis.set('child_cat_list:%s'%category_id,result)

    def del_child_category_list(self,category_id):
        self.redis.delete('child_cat_list:%s'%category_id)

    def delete(self,id):
        result = self.redis.delete('cat:%s'%id)




if __name__== "__main__":
    pass