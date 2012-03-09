# -*- coding: utf-8 -*-
import sys
sys.path.append("d:\python\sharejs")

from mysqldb import DB
from model.article import  Article

class ArticleRepository(DB):
    def __init__(self):
        DB.__init__(self)

    def search(self,category_id=0,recommend=0,topic_id=0,keyword=None,order='id desc',state=1,start=0,count=10,fields='*'):
        result = {}
        condition = ' 1=1 '
        if category_id:
            condition += ' and (root_category_id=%(category_id)s or category_id=%(category_id)s)'
        if recommend:
            condition += ' and recommend=%(recommend)s'
        if topic_id:
            condition += ' and topic_id=%(topic_id)s'
        if keyword:
            keyword = '%' + keyword + '%'
            condition += r' and title like %(keyword)s'
        if state>=0:
            condition += r' and state =%(state)s'


        params = {
            'category_id':category_id,
            'recommend':recommend,
            'topic_id':topic_id,
            'keyword':keyword,
            'state':state,
            'start':start,
            'size':count,
        }

        self.cursor.execute('select count(*) as count from article where %s'%condition,params)
        result['total_count']=self.cursor.fetchone().get('count',0)
        self.cursor.execute('select ' + fields + ' from article where ' + condition + ' order by ' + order + ' limit %(start)s,%(size)s ',params)
        result['list'] = map(lambda row: Article(row), self.cursor.fetchall())
        return result

    def get_data(self,id):
        self.cursor.execute('select * from article where id=%(id)s',{'id':id})
        result= self.cursor.fetchone()
        if result:
            return Article(result)
        else:
            return None

    def get_prev_data(self,id,fields='*'):
        self.cursor.execute('select ' + fields + ' from article where id<%(id)s and state=1 order by id desc limit 1',{'id':id})
        data = self.cursor.fetchone()
        if data:
            return Article(data)
        else:
            return None



    def get_next_data(self,id,fields='*'):
        self.cursor.execute('select ' + fields + ' from article where id>%(id)s and state=1 order by id asc limit 1',{'id':id})
        data = self.cursor.fetchone()
        if data:
            return Article(data)
        else:
            return None

    def delete(self,id):
        self.cursor.execute('delete from article where id=%(id)s',{'id':id})
        self.cursor.connection.commit()

    def update_recommend(self,id):
        self.cursor.execute('update article set recommend=1-recommend where id=%(id)s',{'id':id})
        self.cursor.connection.commit()

    def insert(self,article):
        self.cursor.execute(
            '''
                insert into article
                    (rootcategory_id,
                     category_id,
                     category_id2,
                     category_id3,
                     title,
                     author,
                     source,
                     short_description,
                     description,
                     demo_code,
                     dev_view_code,
                     full_download_url,
                     head_code,
                     body_code,
                     demo_url,
                     compatibility,
                     recommend,
                     pic,
                     small_pic,
                     topic_id,
                     state,
                     isrtdate,
                     last_hit_date,
                     hits
                    )
                values
                    (
                     %(root_category_id)s,
                     %(category_id)s,
                     %(category_id2)s,
                     %(category_id3)s,
                     %(title)s,
                     %(author)s,
                     %(source)s,
                     %(short_description)s,
                     %(description)s,
                     %(demo_code)s,
                     %(dev_view_code)s,
                     %(full_download_url)s,
                     %(head_code)s,
                     %(body_code)s,
                     %(demo_url)s,
                     %(compatibility)s,
                     %(recommend)s,
                     %(pic)s,
                     %(small_pic)s,
                     %(topic_id)s,
                     %(state)s,
                     %(isrtdate)s,
                     %(last_hit_date)s,
                     %(hits)s
                    )
            ''',article.__dict__
        )
        self.cursor.connection.commit()
        self.cursor.execute('select last_insert_id() as id')
        return self.cursor.fetchone().get('id',0)

    def update(self,article):
        self.cursor.execute('''update article set root_category_id=%(root_category_id)s,
                                             category_id=%(category_id)s,
                                             category_id2=%(category_id2)s,
                                             category_id3=%(category_id3)s,
                                             title=%(title)s,
                                             author=%(author)s,
                                             source=%(source)s,
                                             short_description=%(short_description)s,
                                             description=%(description)s,
                                             demo_code=%(demo_code)s,
                                             demo_url=%(demo_url)s,
                                             dev_view_code=%(dev_view_code)s,
                                             full_download_url=%(full_download_url)s,
                                             head_code=%(head_code)s,
                                             body_code=%(body_code)s,
                                             compatibility=%(compatibility)s,
                                             recommend=%(recommend)s,
                                             pic=%(pic)s,
                                             small_pic=%(small_pic)s,
                                             topic_id=%(topic_id)s,
                                             state=%(state)s,
                                             hits=%(hits)s,
                                             isrtdate=%(isrtdate)s,
                                             last_hit_date=%(last_hit_date)s

                                where id=%(id)s
                                             ''',article.__dict__)
        self.cursor.connection.commit()
        return article.id

    def update_hits(self,id):
        self.cursor.execute("update article set hits=hits+1 ,last_hit_date=curdate() where id=%(id)s",{'id':id})
        self.cursor.connection.commit()

    def update_download(self,id):
        self.cursor.execute("update article set download=download+1  where id=%(id)s",{'id':id})
        self.cursor.connection.commit()


    def update_state(self,id):
        self.cursor.execute('update article set state=1-state where id=%(id)s',{'id':id})
        self.cursor.connection.commit()

    def get_total_hits(self):
        self.cursor.execute('select sum(hits) as sum_hits from article')
        return self.cursor.fetchone().get('sum_hits',0)

    def get_total_download(self):
        self.cursor.execute('select sum(download) as sum_download from article')
        return self.cursor.fetchone().get('sum_download',0)

    def update_smallpic(self,id,small_pic):
        self.cursor.execute('update article set small_pic=:small_pic where id=%(id)s',{'id':id,'small_pic':small_pic})
        self.cursor.connection.commit()

if __name__== "__main__":
    article_repository = ArticleRepository()
    articles = article_repository.search(category_id=100)['list']
    for article in articles:
        print(article.title)
