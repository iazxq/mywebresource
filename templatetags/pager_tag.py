# -*- coding: utf-8 -*-
from django import template

register = template.Library()

@register.inclusion_tag('common/pager.html', takes_context=True)
def pager_tag(context,pager):
    return {'pager':pager}

