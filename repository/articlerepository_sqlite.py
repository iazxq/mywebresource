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
            condition += ' and (rootcategoryid=%(categoryid)s or categoryid=%(categoryid)s)'
        if recommend:
            condition += ' and recommend=%(recommend)s'
        if topic_id:
            condition += ' and topicid=:topicid'
        if keyword:
            keyword = '%' + keyword + '%'
            condition += r' and title like :keyword'
        if state>=0:
            condition += r' and state =:state'


        params = {
            'categoryid':category_id,
            'recommend':recommend,
            'topicid':topic_id,
            'keyword':keyword,
            'state':state,
            'start':start,
            'size':count,
        }

        self.cursor.execute('select count(*) as count from js where %s'%condition,params)
        result['total_count']=self.cursor.fetchone().get('count',0)
        self.cursor.execute('select %s from js where %s order by %s limit :start,:size '%(fields,condition,order),params)
        result['list'] = map(lambda row: Article(row), self.cursor.fetchall())
        return result

    def get_data(self,id,state=1):
        self.cursor.execute('select * from js where id=:id',{'id':id,'state':state})
        return Article(self.cursor.fetchone())

    def get_prev_data(self,id,fields='*'):
        self.cursor.execute('select %s from js where id<:id and state=1 order by id desc limit 1'%(fields,),{'id':id})
        data = self.cursor.fetchone()
        if data:
            return Article(data)
        else:
            return None



    def get_next_data(self,id,fields='*'):
        self.cursor.execute('select %s from js where id>:id and state=1 order by id asc limit 1'%(fields,),{'id':id})
        data = self.cursor.fetchone()
        if data:
            return Article(data)
        else:
            return None

    def delete(self,id):
        self.cursor.execute('delete from js where id=:id',{'id':id})
        self.cursor.connection.commit()

    def update_recommend(self,id):
        self.cursor.execute('update js set recommend=1-recommend where id=:id',{'id':id})
        self.cursor.connection.commit()

    def insert(self,article):
        self.cursor.execute(
            '''
                insert into js
                    (rootcategoryid,
                     categoryid,
                     categoryid2,
                     categoryid3,
                     title,
                     author,
                     source,
                     shortdescription,
                     description,
                     democode,
                     devviewcode,
                     fulldownloadurl,
                     headcode,
                     bodycode,
                     demourl,
                     compatibility,
                     recommend,
                     pic,
                     smallpic,
                     topicid,
                     state,
                     isrtdate,
                     lasthitdate,
                     hits
                    )
                values
                    (
                     :root_category_id,
                     :category_id,
                     :category_id2,
                     :category_id3,
                     :title,
                     :author,
                     :source,
                     :short_description,
                     :description,
                     :demo_code,
                     :dev_view_code,
                     :full_download_url,
                     :head_code,
                     :body_code,
                     :demo_url,
                     :compatibility,
                     :recommend,
                     :pic,
                     :small_pic,
                     :topic_id,
                     :state,
                     :isrtdate,
                     :last_hit_date,
                     :hits
                    )
            ''',article.__dict__
        )
        self.cursor.connection.commit()

    def update(self,article):
        self.cursor.execute('''update js set rootcategoryid=:root_category_id,
                                             categoryid=:category_id,
                                             categoryid2=:category_id2,
                                             categoryid3=:category_id3,
                                             title=:title,
                                             author=:author,
                                             source=:source,
                                             shortdescription=:short_description,
                                             description=:description,
                                             democode=:demo_code,
                                             demourl=:demo_url,
                                             devviewcode=:dev_view_code,
                                             fulldownloadurl=:full_download_url,
                                             headcode=:head_code,
                                             bodycode=:body_code,
                                             compatibility=:compatibility,
                                             recommend=:recommend,
                                             pic=:pic,
                                             smallpic=:small_pic,
                                             topicid=:topic_id,
                                             state=:state,
                                             hits=:hits,
                                             isrtdate=:isrtdate,
                                             lasthitdate=:last_hit_date

                                where id=:id
                                             ''',article.__dict__)
        self.cursor.connection.commit()

    def update_hits(self,id):
        self.cursor.execute("update js set hits=hits+1 ,lasthitdate=(datetime('now', 'localtime')) where id=%(id)s",{'id':id})
        self.cursor.connection.commit()

    def update_download(self,id):
        self.cursor.execute("update js set download=download+1  where id=:id",{'id':id})
        self.cursor.connection.commit()


    def update_state(self,id):
        self.cursor.execute('update js set state=1-state where id=:id',{'id':id})
        self.cursor.connection.commit()

    def get_total_hits(self):
        self.cursor.execute('select sum(hits) as sum_hits from js')
        return self.cursor.fetchone().get('sum_hits',0)

    def get_total_download(self):
        self.cursor.execute('select sum(download) as sum_download from js')
        return self.cursor.fetchone().get('sum_download',0)

    def update_smallpic(self,id,small_pic):
        self.cursor.execute('update js set smallpic=:smallpic where id=:id',{'id':id,'smallpic':small_pic})
        self.cursor.connection.commit()

if __name__== "__main__":
    article_repository = ArticleRepository()
    articles = article_repository.search(category_id=100)
    list = articles['list']
    for article in list:
        print(article.__dict__)
