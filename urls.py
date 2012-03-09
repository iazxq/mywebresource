# -*- coding: utf-8 -*-
#Url路由
from django.conf.urls.defaults import *
import os.path
import re
import views.home
import views.admin


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^pdbooks/', include('pdbooks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #admin urls
    (r'admin/',include('views.admin.urls')),
    
    url(r'^$', views.home.index,name='index'),
    url(r'^subject/(\d+)$',views.home.detail,name='detail'),
    url(r'^category/(\d+)$',views.home.category,name='category'),
    url(r'^category/(\d+)/(pic|text)$',views.home.category,name='category'),
    url(r'^topic/(\d+)$',views.home.topic,name='topic'),
    url(r'^search$',views.home.search,name='search'),
    url(r'^search/(pic|text)$',views.home.search,name='search'),
    url(r'^tag/(.+)$',views.home.tag,name='tag'),
    url(r'^subject/(\d+)/recommend$',views.home.recommend,name='subject.recommend'),
    url(r'^subject/(\d+)/devviewcode$',views.home.devviewcode,name='subject.devviewcode'),
    url(r'^download/(\d+)$',views.home.download,name='download'),

    url(r'^js$',views.home.js,name='js'),
    url(r'^code$',views.home.code,name='code'),
    url(r'^tutorial$',views.home.tutorial,name='tutorial'),
    url(r'^software$',views.home.software,name='software'),
    url(r'^tools$',views.home.tools,name='tools'),
    url(r'^jquery$',views.home.jquery,name='jquery'),
    url(r'^JQuery$',views.home.jquery),
    url(r'^goodsites$',views.home.goodsites,name='goodsites'),
    url(r'^pngs$',views.home.pngs,name='png'),
    url(r'^vectors$',views.home.vectors,name='vector'),
    url(r'^template$',views.home.template,name='template'),
    
    #define static routes
    (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  os.path.join(os.path.dirname(__file__), 'css').replace('\\','/'),}),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  os.path.join(os.path.dirname(__file__), 'images').replace('\\','/'),}),
    (r'^scripts/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  os.path.join(os.path.dirname(__file__), 'scripts').replace('\\','/'),}),
    (r'^tools/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  os.path.join(os.path.dirname(__file__), 'tools').replace('\\','/'),}),
    (r'^up/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  os.path.join(os.path.dirname(__file__), 'up').replace('\\','/'),}),
    (r'^uploadfiles/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  os.path.join(os.path.dirname(__file__), 'uploadfiles').replace('\\','/'),}),
    (r'^UploadFiles/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  os.path.join(os.path.dirname(__file__), 'uploadfiles').replace('\\','/'),}),
    (r'^software/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  os.path.join(os.path.dirname(__file__), 'software').replace('\\','/'),}),
    (r'^code/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  os.path.join(os.path.dirname(__file__), 'code').replace('\\','/'),}),
    (r'^vectors/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  os.path.join(os.path.dirname(__file__), 'vectors').replace('\\','/'),}),
    (r'^pngs/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  os.path.join(os.path.dirname(__file__), 'pngs').replace('\\','/'),}),
    (r'^template/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  os.path.join(os.path.dirname(__file__), 'template').replace('\\','/'),}),
    (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root':  os.path.join(os.path.dirname(__file__), 'js').replace('\\','/'),}),

    #以下rewrite是为了兼容以前的.net 程序的地址
    (r'^code\.aspx$',views.home.code),
    (r'^tutorial\.aspx$',views.home.tutorial),
    (r'^software\.aspx$',views.home.software),
    (r'^tools\.aspx$',views.home.tools),
    (r'^jquery\.aspx$',views.home.jquery),
    (r'^JQuery\.aspx$',views.home.jquery),
    (r'^goodsites\.aspx$',views.home.goodsites),
    (r'^pngs\.aspx$',views.home.pngs),
    (r'^vectors\.aspx$',views.home.vectors),
    (r'^showdetails-(\d+).aspx$',views.home.detail),
    (r'^commondetails-(\d+).aspx$',views.home.detail),
    (r'^tooldetails-(\d+).aspx$',views.home.detail),
    (r'^pngdetails-(\d+).aspx$',views.home.detail),
    (r'^vectordetails-(\d+).aspx$',views.home.detail),
    (r'^cat-(\d+)\.aspx$',views.home.category),
    (r'^topic-(\d+)\.aspx$',views.home.topic),
    (r'^search\.aspx$',views.home.search),
    (r'^list\.aspx$',views.home.index),
    (r'^recommend-(\d+)\.aspx$',views.home.recommend),
)
