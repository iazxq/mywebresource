# -*- coding: utf-8 -*-

from repository.categoryrepository import CategoryRepository
from repository.categoryredis import CategoryRedis

class CategoryFacade:
    def __init__(self):
        self.category_repository = CategoryRepository()
        self.category_redis = CategoryRedis()

    def get_data(self,category_id,get_detail=True):
        '''
        get_detail 是否需要获得分类的更详细信息
        '''
        category = None
        category = self.category_redis.get_data(category_id)
        if not category:
            category = self.category_repository.get_data(category_id)
            self.category_redis.set_data(category)

        #获取分类的上级分类和根分类信息
        if get_detail:
            if  category:
                if category.parent_category_id:
                    category.parent_category = self.get_data(category.parent_category_id,False)
                category.root_category = self.get_data(category.root_category_id,False)
        return category

    def get_child_category_list(self,category_id):
        result = self.category_redis.get_child_category_list(category_id)
        if not result:
            result = self.category_repository.get_child_category_list(category_id)
            self.category_redis.set_child_category_list(category_id,result)
        return result

    def insert(self,category):
        self.category_repository.insert(category)

    def remove(self,category_id):
        self.category_repository.remove(category_id)
        self.category_redis.delete(category_id)

    def update(self,category):
        self.category_repository.update(category)
        #更新单条分类信息缓存
        self.category_redis.delete(category.category_id)
        #更新其上级分类的子分类
        self.category_redis.del_child_category_list(category.parent_category_id)



if __name__=='__main__':
    category_facade = CategoryFacade()
    print(category_facade.get_child_category_list(800))
