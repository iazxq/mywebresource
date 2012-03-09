# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.inclusion_tag('common/article_list_item_control.html', takes_context=True)
def article_list_item_tag(context,article):
    return {'article':article}

