# -*- coding: utf-8 -*-
from repository.articlerepository import ArticleRepository
from repository.articleredis import ArticleRedis
from repository.categoryrepository import CategoryRepository



class ArticleFacade:
    def __init__(self):
        self.article_repository = ArticleRepository()
        self.article_redis = ArticleRedis()
        self.category_repository = CategoryRepository()

    def get_data(self,id):
        result= self.article_redis.get_data(id)
        if not result:
            result = self.article_repository.get_data(id)
            if result and result.state:
                self.article_redis.set_data(id,result)
        return result

    def get_prev_data(self,id):
        result = None
        article = self.article_repository.get_prev_data(id)
        if article:
            result = self.get_data(article.id)
        return result

    def get_next_data(self,id):
        result = None
        article = self.article_repository.get_next_data(id,fields='id')
        if article:
            result = self.get_data(article.id)
        return result

    def search(self,category_id=0,recommend=0,topic_id=0,keyword=None,order='id desc',state=1,start=0,count=10):
        result = self.article_repository.search(category_id=category_id,topic_id=topic_id,recommend=recommend,keyword=keyword,order=order,state=state,start=start,count=count,fields="id")
        articles = list()
        for article in result['list']:
            article = self.get_data(id=article.id)
            article.category = self.category_repository.get_data(article.category_id)
            articles.append(article)
        result['list'] = articles
        return result



    def delete(self,id):
        self.article_repository.delete(id)
        self.article_redis.delete(id)

    def post_data(self,article):
            if article.id:
                self.article_repository.update(article)
                article = self.article_repository.get_data(article.id)
                self.article_redis.set_data(article.id,article)
                return article.id
            else:
                return self.article_repository.insert(article)

    def update_hits(self,id):
        self.article_repository.update_hits(id)

    def update_download(self,id):
        self.article_repository.update_download(id)

    def update_state(self,id):
        self.article_repository.update_state(id)
        #重新获取信息更新缓存
        article = self.article_repository.get_data(id)
        self.article_redis.set_data(id,article)

    def update_recommend(self,id):
        self.article_repository.update_recommend(id)
        #重新获取信息更新缓存
        article = self.article_repository.get_data(id)
        self.article_redis.set_data(id,article)

    def get_total_hits(self):
        return self.article_repository.get_total_hits()

    def get_total_download(self):
        return self.article_repository.get_total_download()

    def update_smallpic(self,id,small_pic):
        result = self.article_repository.update_smallpic(id,small_pic)
        #重新获取信息更新缓存
        article = self.article_repository.get_data(id)
        self.article_redis.set_data(article)



if __name__=='__main__':
    import factory
    article_facade = factory.create_article_facade()
    javascript_article_list = article_facade.search(category_id=100,count=10)['list']
    for article in javascript_article_list:
        print(article.title)


