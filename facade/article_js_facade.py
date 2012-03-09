# -*- coding: utf-8 -*-
from repository.article_js_repository import ArticleJSRepository


class ArticleJSFacade:
    def __init__(self):
        self.repository_js_repository = ArticleJSRepository()

    def get_data(self,id):
        return self.repository_js_repository.get_data(id)

    def insert(self,article_js):
        self.repository_js_repository.insert(article_js)

    def update(self,article_js):
        self.repository_js_repository.update(article_js)