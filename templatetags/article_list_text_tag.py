# -*- coding: utf-8 -*-
from django import template
import settings
import facade.factory

register = template.Library()

@register.inclusion_tag(settings.DEFAULT_SKIN + '/module/article_list_text.html', takes_context=True)
def article_list_text_tag(context,article_list,category_id,title,end_col):
    '''
    end_col 用于样式，确定是不是一行的最后一列
    '''
    return {'article_list':article_list,
            'title':title,
            'end_col':end_col,
            'category_id':category_id,
            }

