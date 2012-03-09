# -*- coding: utf-8 -*-
from django import template
from django.shortcuts import render_to_response

register = template.Library()

@register.inclusion_tag('common/search_control.html', takes_context=True)
def search_form_tag(context):
    keyword = context.get('keyword','')
    return {'keyword':keyword}

