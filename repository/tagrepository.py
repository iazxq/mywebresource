# -*- coding: utf-8 -*-

from mysqldb import DB
from model.tag import  Tag

class TagRepository(DB):
    def __init__(self):
        DB.__init__(self)

    def insert(self,tag):
        '''
        添加心的tag标签
        '''
        self.cursor.execute('insert into tags(article_id,tag)values(%(article_id)s,%(tag)s)',tag.__dict__)
        self.cursor.connection.commit()

    def remove(self,article_id):
        '''
        删除标签
        '''
        self.cursor.execute('delete from tags where article_id=%(article_id)s',{'article_id':article_id})
        self.cursor.connection.commit()

    def get_tag_list(self,article_id):
        '''
        根据文章编号搜索tag列表
        '''
        params = {  'article_id':article_id }
        self.cursor.execute('select * from tags where article_id=%(article_id)s',params)
        result = map(lambda row: Tag(row), self.cursor.fetchall())
        return result

    def search(self,tag,start=0,count=10):
        '''
        根据tag搜索文章
        '''
        result = {}
        params = {'tag':tag,
                  'start':start,
                  'count':count }
        self.cursor.execute('select count(*) as count from tags where tag=%(tag)s ',params)
        result['total_count'] = self.cursor.fetchone().get('count',0)
        self.cursor.execute('select * from tags where tag=%(tag)s  limit %(start)s,%(count)s',params)
        result['list'] = map(lambda row: Tag(row), self.cursor.fetchall())
        return result

    def get_count(self,tag):
        self.cursor.execute('select count(*) as cnt from tags where tag=%(tag)s',{'tag':tag})
        result =  self.cursor.fetchone()
        return result.get('cnt',0)


if __name__== "__main__":
    tag_repository = TagRepository();
    print(tag_repository.get_count(u'美女'))
    print(tag_repository.get_count(u'色彩'))
