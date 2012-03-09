# -*- coding: utf-8 -*-
import sys
sys.path.append("d:\python\sharejs")


from model.article_js import ArticleJS
from db import DB

class ArticleJSRepository(DB):
    def __init__(self):
        DB.__init__()



    def get_data(self,id):
        self.cursor.execute('select * from article_js where id=%(id)s',{'id':id})
        result = self.cursor.fetchone()
        if result:
            return ArticleJS(result)
        else:
            return None



    def insert(self,article_js):
        self.cursor.execute('''insert into article_js(
                              id,demo_code,demo_url,dev_view_code,head_code,body_code,compatibility
                              )
                              values(
                              %(id)s,%(demo_code)s,%(demo_url)s,%(dev_view_code)s,%(head_code)s,%(body_code)s,%(compatibility)s
                              )''',article_js.__dict__)
        self.cursor.connection.commit()


    def update(self,article_js):
        self.cursor.execute('''update article set
                                demo_code = %(demo_code)s,
                                demo_url = %(demo_url)s,
                                dev_view_code = %(dev_view_code)s,
                                head_code = %(head_code)s,
                                body_code = %(body_code)s,
                                compatibility = %(compatibility)s,
                                where id=%(id)s
                             ''',article_js.__dict__)
        self.cursor.connection.commit()



if __name__== "__main__":
    article_repository = ArticleRepository()
    articles = article_repository.search(category_id=100)['list']
    for article in articles:
        print(article.title)
