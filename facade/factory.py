# -*- coding: utf-8 -*-

from articlefacade import ArticleFacade
from categoryfacade import CategoryFacade
from topicfacade import TopicFacade
from tagfacade import TagFacade
from taghotfacade import TagHotFacade

def create_article_facade():
    return ArticleFacade()

def create_category_facade():
    return CategoryFacade()

def create_topic_facade():
    return TopicFacade()

def create_tag_facade():
    return TagFacade()

def create_taghot_facade():
    return TagHotFacade()