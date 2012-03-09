# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

import datetime

from common import func
from common.pager import Pager

import account
import facade.factory

from model.article import Article

@account.check_login
def index(request):
    return article_list(request)

@account.check_login
def article_list(request):
    '文章管理'
    order = "id desc"
    category_id = func.get_int_param_from_get(request,'category')
    start = func.get_int_param_from_get(request,'start')
    count = 10
    state = -1
    category_facade = facade.factory.create_category_facade()
    category_list = category_facade.get_child_category_list(0)
    article_facade = facade.factory.create_article_facade()
    articles = article_facade.search(category_id=category_id,order=order,state=state,start=start,count=count)
    article_list = articles.get('list',[])
    total_count = articles.get('total_count',0)
    pager = Pager(request,start,count,total_count)
    total_hits = article_facade.get_total_hits()
    total_download = article_facade.get_total_download()
    output = {
        'category_id':category_id,
        'category_list':category_list,
        'article_list':article_list,
        'pager':pager,
        'total_hits':total_hits,
        'total_download':total_download,
    }
    return render_to_response('admin/article_list.html',output)

@account.check_login
def article_edit(request):
    '文章编辑'
    article_facade = facade.factory.create_article_facade()
    topic_facade = facade.factory.create_topic_facade()
    category_facade = facade.factory.create_category_facade()
    tag_facade = facade.factory.create_tag_facade()

    #如果是提交信息
    if request.method =="POST":
        article = Article()
        id = func.get_int_param_from_post(request,'id')
        article.id=id
        article.title = func.get_str_param_from_post(request,'title')
        article.root_category_id = func.get_int_param_from_post(request,'root_category')
        article.category_id = func.get_int_param_from_post(request,'category1')
        article.category_id2 = func.get_int_param_from_post(request,'category2')
        article.category_id3 = func.get_int_param_from_post(request,'category3')
        article.author = func.get_str_param_from_post(request,'author')
        article.source = func.get_str_param_from_post(request,'source')
        article.short_description = func.get_str_param_from_post(request,'short_description')
        article.description = func.get_str_param_from_post(request,'description')
        article.demo_code = func.get_str_param_from_post(request,'demo_code')
        article.demo_url = func.get_str_param_from_post(request,'demo_url')
        article.dev_view_code = func.get_str_param_from_post(request,'dev_view_code')
        article.full_download_url = func.get_str_param_from_post(request,'full_download_url')
        article.head_code = func.get_str_param_from_post(request,'head_code')
        article.body_code = func.get_str_param_from_post(request,'body_code')
        article.compatibility = func.get_str_param_from_post(request,'compatibility')
        article.pic = func.get_str_param_from_post(request,'pic')
        article.small_pic = func.get_str_param_from_post(request,'small_pic')
        article.recommend = func.get_str_param_from_post(request,'recommend')=='on'
        article.topic_id = func.get_str_param_from_post(request,'topic_id')
        article.state = 0
        article.isrtdate = func.format_date_time(func.str_to_datetime(func.get_str_param_from_post(request,'isrtdate')))
        article.last_hit_date=func.format_date_time(func.str_to_datetime(func.get_str_param_from_post(request,'last_hit_date')))
        article.hits = func.get_int_param_from_post(request,'hits')

        id = article_facade.post_data(article)
        #添加Tags
        tag_facade.insert_tags(id,func.get_str_param_from_post(request,'tags'))

        refer_url = func.get_str_param_from_post(request,'refer_url')
        if not refer_url:
            refer_url = "article_list"

        return HttpResponseRedirect(refer_url)
        

    id = func.get_int_param_from_get(request,'id')
    output = {}

    if id>0:
        article = article_facade.get_data(id)
        article.tags = tag_facade.get_tags_str(id)
        output['article'] = article

    topic_list = topic_facade.get_all_topic()
    root_category_list = category_facade.get_child_category_list(0)
    output['topic_list'] = topic_list
    output['root_category_list'] = root_category_list
    output['refer_url'] = func.get_referer(request,'article_list')
    

    return render_to_response('admin/article_edit.html',output)

@account.check_login
def article_del(request):
    '删除'
    id = int(request.GET.get('id',0))
    article_facade = facade.factory.create_article_facade()
    article_facade.delete(id)
    return_url = func.get_referer(request,'article_list')
    return HttpResponseRedirect(return_url)

@account.check_login
def article_update_recommend(request):
    '删除'
    id = int(request.GET.get('id',0))
    article_facade = facade.factory.create_article_facade()
    article_facade.update_recommend(id)
    return_url = func.get_referer(request,'article_list')
    return HttpResponseRedirect(return_url)

@account.check_login
def article_update_state(request):
    '删除'
    id = int(request.GET.get('id',0))
    article_facade = facade.factory.create_article_facade()
    article_facade.update_state(id)
    return_url = func.get_referer(request,'article_list')
    return HttpResponseRedirect(return_url)