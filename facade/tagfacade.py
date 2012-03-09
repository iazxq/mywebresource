# -*- coding: utf-8 -*-
from repository.tagrepository import TagRepository
import facade.factory
from model.tag import Tag




class TagFacade:
    def __init__(self):
        self.tag_repository = TagRepository()
        self.article_facade = facade.factory.create_article_facade()
        self.category_facade = facade.factory.create_category_facade()
        self.taghot_facade = facade.factory.create_taghot_facade()

    def get_tag_list(self,article_id):
        return self.tag_repository.get_tag_list(article_id)

    def search(self,tag,start=0,count=10):
        '''
        搜索,返回文章列表
        '''
        result = self.tag_repository.search(tag=tag,start=start,count=count)
        article_list = list()
        for tag in result['list']:
            article = self.article_facade.get_data(id=tag.article_id)
            if article and article.state:
                article.category = self.category_facade.get_data(article.category_id)
                article_list.append(article)

        result['list'] = article_list
        return result

    def get_tags_str(self,article_id):
        result = ''
        tag_list = self.tag_repository.get_tag_list(article_id)
        if tag_list:
            for tag in tag_list:
                result += tag.tag + ','
            if result:
                result = result[:-1]
        return result

    def insert_tags(self,article_id,tags):
        '''
        按字符串批量添加tag,tag之间用逗号隔开
        '''
        tags = tags.replace('，',',').replace('|',',')
        tag_str_list = tags.split(',')
        if tag_str_list:
            self.remove(article_id)
            for str in tag_str_list:
                if str:
                    self.insert(Tag(article_id=article_id,tag=str))
                    hot = self.get_count(str)
                    print('tag=%s,hot=%s'%(str,hot))
                    self.taghot_facade.post_tag(tag=str,hot=hot)


    def remove(self,article_id):
        self.tag_repository.remove(article_id)

    def insert(self,tag):
        self.tag_repository.insert(tag)


    def get_count(self,tag):
        return self.tag_repository.get_count(tag)



if __name__=='__main__':
    tag_facade = TagFacade()
    tag_facade.insert_tags(1,'色彩,美女')
    print(tag_facade.get_count(u'色彩'))
    print(tag_facade.get_count(u'美女'))

