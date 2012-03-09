from django.conf.urls.defaults import *
import os.path

import account
import index
import article
import category

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', index.index),
    (r'^login$',account.login),
    (r'^logout$',account.logout),
    (r'^article$',article.index),
    (r'^article_list$',article.index),
    (r'^article_edit$',article.article_edit),
    (r'^article_del$',article.article_del),
    url(r'^article_update_state$',article.article_update_state,name="admin.article_update_state"),
    url(r'^article_update_recommend$',article.article_update_recommend,name="admin.article_update_recommend"),
    (r'^get_child_category_list/(\d+)$',category.get_child_category_list),
    url(r'^category$',category.index,name="admin.category_list"),
    url(r'^category_edit$',category.edit,name="admin.category_edit"),
    url(r'^category_remove$',category.remove,name="admin.category_remove"),

)
