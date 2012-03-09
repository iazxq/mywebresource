# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.views.decorators.cache import cache_page
from django.core.cache import cache

import random

from common import func
from common.pager import Pager

import settings

import facade.factory

#@cache_page(60 * 60)
def index(request):
    article_facade = facade.factory.create_article_facade()
    category_facade = facade.factory.create_category_facade()
    topic_facade = facade.factory.create_topic_facade()

    javascript_article_list = article_facade.search(category_id=100,count=10)['list']
    recommend_javascript_article_list = article_facade.search(category_id=100,recommend=1,count=5)['list']
    hot_javascript_article_list = article_facade.search(category_id=100,order='hits desc',count=10)['list']

    png_article_list = article_facade.search(category_id=600,count=10)['list']

    vector_article_list = article_facade.search(category_id=700,count=10)['list']
    recommend_vector_article_list = article_facade.search(category_id=700,recommend=1,count=8)['list']

    template_article_list = article_facade.search(category_id=800,count=10)['list']
    recommend_template_article_list = article_facade.search(category_id=800,recommend=1,count=8)['list']
    hot_template_article_list = article_facade.search(category_id=800,order='hits desc',count=10)['list']

    recommend_article_pic_list = article_facade.search(recommend=1,count=12)['list']

    article_list = article_facade.search(count=18)['list']
    js_category_list = category_facade.get_child_category_list(100)
    recommend_article_list = article_facade.search(recommend=1,count=20)['list']
    top_hits_article_list = article_facade.search(order='hits desc',count=20)['list']
    last_hit_article_list = article_facade.search(order='last_hit_date desc',count=50)['list']
    last_article_list = article_facade.search(count=50)['list']

    topic_list = topic_facade.get_all_topic()

    output = {
        'recommend_article_pic_list':recommend_article_pic_list,
        'javascript_article_list':javascript_article_list,
        'recommend_javascript_article_list':recommend_javascript_article_list,
        'hot_javascript_article_list':hot_javascript_article_list,
        'template_article_list':template_article_list,
        'recommend_template_article_list':recommend_template_article_list,
        'hot_template_article_list':hot_template_article_list,
        'png_article_list':png_article_list,
        'vector_article_list':vector_article_list,
        'recommend_vector_article_list':recommend_vector_article_list,
        'article_list':article_list,
        'js_category_list':js_category_list,
        'recommend_article_list':recommend_article_list,
        'top_hits_article_list':top_hits_article_list,
        'last_hit_article_list':last_hit_article_list,
        'last_article_list':last_article_list,
        'topic_list':topic_list,
        'request':request,
    }
    return render_to_response('%s/index.html'%settings.DEFAULT_SKIN,output)

@cache_page(60*60)
def js(request):
    article_facade = facade.factory.create_article_facade()
    recommend_article_pic_list = article_facade.search(recommend=1,category_id=132,count=12)['list']

    hot_javascript_article_list = article_facade.search(category_id=100,order='hits desc',count=12)['list']
    hot_template_article_list = article_facade.search(category_id=800,order='hits desc',count=12)['list']

    article_list_color = article_facade.search(category_id=110, count=10)['list']
    article_list_link = article_facade.search(category_id=111, count=10)['list']
    article_list_text = article_facade.search(category_id=112, count=10)['list']
    article_list_css = article_facade.search(category_id=113, count=10)['list']
    article_list_table = article_facade.search(category_id=114, count=10)['list']
    article_list_math = article_facade.search(category_id=115, count=10)['list']
    article_list_windows = article_facade.search(category_id=116, count=10)['list']
    article_list_menu = article_facade.search(category_id=117, count=10)['list']
    article_list_scroll = article_facade.search(category_id=118, count=10)['list']
    article_list_image = article_facade.search(category_id=119, count=10)['list']
    article_list_date = article_facade.search(category_id=129, count=10)['list']
    article_list_mouse = article_facade.search(category_id=121, count=10)['list']
    article_list_keyboard = article_facade.search(category_id=122, count=10)['list']
    article_list_button = article_facade.search(category_id=123, count=10)['list']
    article_list_status = article_facade.search(category_id=124, count=10)['list']
    article_list_other = article_facade.search(category_id=125, count=10)['list']
    article_list_system = article_facade.search(category_id=126, count=10)['list']
    article_list_cookie = article_facade.search(category_id=127, count=10)['list']
    article_list_form = article_facade.search(category_id=128, count=10)['list']
    article_list_game = article_facade.search(category_id=129, count=10)['list']
    article_list_reg = article_facade.search(category_id=130, count=10)['list']
    article_list_ajax = article_facade.search(category_id=131, count=10)['list']
    article_list_ad = article_facade.search(category_id=132, count=10)['list']
    article_list_drag = article_facade.search(category_id=133, count=10)['list']
    article_list_components = article_facade.search(category_id=134, count=10)['list']
    article_list_player = article_facade.search(category_id=135, count=10)['list']
    article_list_layout = article_facade.search(category_id=136, count=10)['list']
    article_list_html5 = article_facade.search(category_id=757, count=10)['list']

    return render_to_response(settings.DEFAULT_SKIN+'/js.html',locals())

def detail(request,id):
    article_facade = facade.factory.create_article_facade()
    tag_facade = facade.factory.create_tag_facade()
    article = article_facade.get_data(id)

    if article.state != 1:
        return redirect('/')

    prev_article = article_facade.get_prev_data(id)
    next_article = article_facade.get_next_data(id)

    category_facade = facade.factory.create_category_facade()
    category = category_facade.get_data(article.category_id)

    #从缓存读取
    recommend_article_list = cache.get('recommend_article_list_%s'%category.category_id)
    if not recommend_article_list:
        recommend_article_list = article_facade.search(category_id=category.category_id,recommend=1)['list']
        cache.set('recommend_article_list_%s'%category.category_id,recommend_article_list,60*60*24*30)

    hot_article_list = cache.get('hot_article_list_%s'%category.category_id)
    if not hot_article_list:
        hot_article_list = article_facade.search(category_id=category.category_id,order='hits desc')['list']
        cache.set('hot_article_list_%s'%category.category_id,hot_article_list,60*60*24*30)

    new_article_list = cache.get('new_article_list_%s'%category.category_id)
    if not new_article_list:
        new_article_list = article_facade.search(category_id=category.category_id,order='id desc')['list']
        cache.set('new_article_list_%s'%category.category_id,new_article_list,60*60*24*30)

    all_recommend_article_list = article_facade.search(category_id=category.root_category_id,recommend=1,count=3,order='rand()')['list']
    all_recommend_article_list.insert(random.randint(0,3),None)

    tag_list = tag_facade.get_tag_list(id)

    output = {
        'article':article,
        'prev_article':prev_article,
        'next_article':next_article,
        'category':category,
        'hot_article_list':hot_article_list,
        'new_article_list':new_article_list,
        'recommend_article_list':recommend_article_list,
        'all_recommend_article_list':all_recommend_article_list,
        'tag_list':tag_list,
    }

    template = settings.DEFAULT_SKIN+'/detail.html'
    '''
    if category.root_category_id in (700,600):
         template = settings.DEFAULT_SKIN+'/vector_detail.html'
    '''

    #增加一次点击计数
    article_facade.update_hits(id)

    return render_to_response(template,output)

def devviewcode(request,id):
    article_facade = facade.factory.create_article_facade()
    article = article_facade.get_data(id)

    category_facade = facade.factory.create_category_facade()
    category = category_facade.get_data(article.category_id)

    recommend_article_list = article_facade.search(category_id=category.category_id,recommend=1)['list']
    hot_article_list = article_facade.search(category_id=category.category_id,order='hits desc')['list']

    output = {
        'article':article,
        'category':category,
        'recommend_article_list':recommend_article_list,
        'hot_article_list':hot_article_list,
    }
    return render_to_response(settings.DEFAULT_SKIN+'/dev_view_code.html',output)

def recommend(request,id):
    article_facade = facade.factory.create_article_facade()
    article = article_facade.get_data(id)

    category_facade = facade.factory.create_category_facade()
    category = category_facade.get_data(article.category_id)

    recommend_article_list = article_facade.search(category_id=category.category_id,recommend=1)['list']
    hot_article_list = article_facade.search(category_id=category.category_id,order='hits desc')['list']

    output = {
        'article':article,
        'category':category,
        'recommend_article_list':recommend_article_list,
        'hot_article_list':hot_article_list,
    }
    return render_to_response(settings.DEFAULT_SKIN + '/recommend.html',output)

def category(request,category_id,list_type='pic'):
    '分类浏览文章'
    start = func.get_int_param_from_get(request,'start')
    count = 20
    article_facade = facade.factory.create_article_facade()
    articles = article_facade.search(category_id=category_id,start=start,count=count)
    article_list = articles['list']
    total_count = int(articles['total_count'])
    pager = Pager(request,start,page_size=count,total_count=total_count)
    #为article_list添加广告代码
    ad_list = (random.randint(0,10),random.randint(0,10))
    for ad in ad_list:
        article_list.insert(ad,None)

    #热门文章
    hot_article_list = article_facade.search(category_id=category_id,order='hits desc')['list']
    recommend_article_list = article_facade.search(category_id=category_id,recommend=1)['list']

    #类别列表
    category_facade = facade.factory.create_category_facade()
    category = category_facade.get_data(category_id)
    category_list = category_facade.get_child_category_list(category.root_category_id)

    #专题
    topic_facade = facade.factory.create_topic_facade()
    topic_list = topic_facade.get_all_topic()

    output = {
        'article_list' : article_list,
        'hot_article_list' : hot_article_list,
        'recommend_article_list':recommend_article_list,
        'category_list' : category_list,
        'category':category,
        'pager' : pager,
        'topic_list':topic_list,
    }
    template_file = 'category.html'
    if list_type=='text':
        template_file = 'category_text.html'
    return render_to_response(settings.DEFAULT_SKIN + '/' + template_file,output)


def topic(request,topic_id):
    '专题文章'
    start = func.get_int_param_from_get(request,'start')
    count = 20
    article_facade = facade.factory.create_article_facade()
    articles = article_facade.search(topic_id=topic_id,start=start,count=count)
    article_list = articles['list']
    total_count = int(articles['total_count'])
    pager = Pager(request,start,page_size=count,total_count=total_count)

    #为article_list添加广告代码
    ad_list = (random.randint(0,10),random.randint(0,10))
    for ad in ad_list:
        article_list.insert(ad,None)

    #热门文章
    hot_article_list = article_facade.search(topic_id=topic_id,order='hits desc')['list']
    #推荐文章
    recommend_article_list = article_facade.search(topic_id=topic_id,recommend=1)['list']

    #专题
    topic_facade = facade.factory.create_topic_facade()
    topic_list = topic_facade.get_all_topic()
    topic = topic_facade.get_data(topic_id)

    output = {
        'article_list' : article_list,
        'hot_article_list' : hot_article_list,
        'recommend_article_list':recommend_article_list,
        'topic':topic,
        'pager' : pager,
        'topic_list':topic_list,
    }
    return render_to_response(settings.DEFAULT_SKIN+'/topic.html',output)

def search(request,list_type='text'):
    start = func.get_int_param_from_get(request,'start')
    count = 20
    keyword = request.GET.get('wd','')
    article_facade = facade.factory.create_article_facade()
    articles = article_facade.search(keyword=keyword,start=start,count=count)
    article_list = articles['list']
    total_count = int(articles['total_count'])
    pager = Pager(request,start,page_size=count,total_count=total_count)


    #推荐文章
    recommend_article_list = article_facade.search(recommend=1)['list']
    #热门文章
    hot_article_list = article_facade.search(order='hits desc')['list']

    #专题
    topic_facade = facade.factory.create_topic_facade()
    topic_list = topic_facade.get_all_topic()

    output = {
        'article_list' : article_list,
        'recommend_article_list':recommend_article_list,
        'hot_article_list' : hot_article_list,
        'pager' : pager,
        'topic_list':topic_list,
        'keyword':keyword,
    }
    template_file = 'search_text.html'
    if list_type=='pic':
        template_file = 'search.html'
    return render_to_response(settings.DEFAULT_SKIN + '/' + template_file,output)

def tag(request,tag):
    start = func.get_int_param_from_get(request,'start')
    count = 20
    list_type='text'
    tag_facade = facade.factory.create_tag_facade()
    article_facade = facade.factory.create_article_facade()
    taghot_facade = facade.factory.create_taghot_facade()

    articles = tag_facade.search(tag=tag,start=start,count=count)
    article_list = articles['list']
    total_count = int(articles['total_count'])
    pager = Pager(request,start,page_size=count,total_count=total_count)


    #推荐文章
    recommend_article_list = article_facade.search(recommend=1)['list']
    #热门文章
    hot_article_list = article_facade.search(order='hits desc')['list']

    #专题
    topic_facade = facade.factory.create_topic_facade()
    topic_list = topic_facade.get_all_topic()

    tag_hot_list = taghot_facade.get_hot_list(count=20)


    output = {
        'article_list' : article_list,
        'recommend_article_list':recommend_article_list,
        'hot_article_list' : hot_article_list,
        'pager' : pager,
        'topic_list':topic_list,
        'tag':tag,
        'tag_hot_list':tag_hot_list
        }
    template_file = 'tag.html'
    if list_type=='pic':
        template_file = 'tag.html'
    return render_to_response(settings.DEFAULT_SKIN + '/' + template_file,output)

def download(request,id):
    article_facade = facade.factory.create_article_facade()
    article = article_facade.get_data(id)
    if article.full_download_url:
        article_facade.update_download(id)
        if article.full_download_url.endswith('.zip') or article.full_download_url.endswith('.rar'):
            download_url = 'img.t.bandao.cn/i/js/%s'%article.full_download_url
            download_url = 'http://' + download_url.replace('//','/')
            return redirect(download_url)
        else:
            return redirect(article.full_download_url)

def code(request):
    return category(request,100)

def tutorial(request):
    return category(request,500,'text')

def software(request):
    return category(request,300)

def tools(request):
    return category(request,200)

def jquery(request):
    return category(request,400)

def goodsites(request):
    return category(request,303)

def pngs(request):
    return category(request,600)

def vectors(request):
    return category(request,700)

def template(request):
    return category(request,800)


if __name__=='__main__':
    article_facade = facade.factory.create_article_facade()
    javascript_article_list = article_facade.search(category_id=100,count=10)['list']
    for article in javascript_article_list:
        print(article.title)