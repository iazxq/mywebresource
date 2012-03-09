# -*- coding: utf-8 -*-
from django import template
import settings
import facade.factory

register = template.Library()

@register.inclusion_tag(settings.DEFAULT_SKIN + '/module/recommend_article_pic_list.html', takes_context=True)
def recommend_article_pic_list_tag(context,article_list):
    return {'article_list':article_list}

