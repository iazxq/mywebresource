# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
import json

from common import func
from common.pager import Pager

import facade.factory
from model.article import Article
from model.category import  Category

import account


@account.check_login
def index(request):
    parent_category_id = func.get_int_param_from_get(request,'parent_category_id')
    category_facade = facade.factory.create_category_facade()
    parent_category = category_facade.get_data(parent_category_id)
    category_list = category_facade.get_child_category_list(parent_category_id)
    return render_to_response('admin/category_list.html',locals())

@account.check_login
def edit(request):
    category_facade = facade.factory.create_category_facade()

    if request.method =="POST":
        category_id = func.get_int_param_from_post(request,'category_id')
        old_category = category_facade.get_data(category_id)
        category = Category()
        if old_category:
            category = old_category
        category.category_id = func.get_int_param_from_post(request,'category_id')
        category.category_name = func.get_str_param_from_post(request,'category_name')
        category.parent_category_id = func.get_int_param_from_post(request,'parent_category_id')
        category.root_category_id = func.get_int_param_from_post(request,'root_category_id')
        category.article_type = func.get_int_param_from_post(request,'article_type')
        category.description = func.get_str_param_from_post(request,'description')

        if old_category:
            category_facade.update(category)
        else:
            category_facade.insert(category)
        return HttpResponseRedirect('category?parent_category_id=%s'%category.parent_category_id)


    category_id = func.get_int_param_from_get(request,'category_id')
    category = category_facade.get_data(category_id)

    parent_category_id = func.get_int_param_from_get(request,'parent_category_id')
    parent_category = category_facade.get_data(parent_category_id)
    if category:
        parent_category = category_facade.get_data(category.parent_category_id)
    
    root_category_id = 0
    if parent_category:
        root_category_id = parent_category.root_category_id
    root_category = category_facade.get_data(root_category_id)

    if not category:
        category = Category()
        category.root_category_id = root_category_id
        category.parent_category_id = parent_category_id

    
    return render_to_response('admin/category_edit.html',locals())

@account.check_login
def remove(request):
    category_id = func.get_int_param_from_get(request,'category_id')
    category_facade = facade.factory.create_category_facade()
    category = category_facade.get_data(category_id)
    category_facade.remove(category_id)
    return HttpResponseRedirect('category?parent_category_id=%s'%category.parent_category_id)


@account.check_login
def get_child_category_list(request,root_category_id):
    category_facade = facade.factory.create_category_facade()
    category_list = category_facade.get_child_category_list(root_category_id)

    #将列表转换成字典格式，方便json输出
    category_dict_list = list()
    for category in category_list:
        category_dict_list.append(category.format_data())
    return HttpResponse(json.dumps(category_dict_list))
