# -*- coding: utf-8 -*-
'''
 * 创建: dfugo
 * 日期: 12-1-16
 × 注释:
'''


from django import template
import settings
import facade.factory

register = template.Library()

@register.inclusion_tag(settings.DEFAULT_SKIN + '/module/last_article_list.html', takes_context=True)
def last_article_list_tag(context,category_id=0):
    article_facade = facade.factory.create_article_facade()
    article_list = article_facade.search(category_id=category_id,count=10)['list']
    return {'article_list':article_list}

