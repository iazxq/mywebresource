# -*- coding: utf-8 -*-
from django import template
import facade.factory

register = template.Library()

@register.inclusion_tag('common/topic_list_control.html', takes_context=True)
def topic_list_tag(context):
    topic_facade = facade.factory.create_topic_facade()
    topic_list = topic_facade.get_all_topic()
    return {'topic_list':topic_list}

