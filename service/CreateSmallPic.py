# -*- coding: utf-8 -*-

import Image, ImageEnhance,os,sys,glob
import facade.factory


article_facade = facade.factory.create_article_facade()
article_list = article_facade.search(count=100000,state=-1)['list']
for article in article_list:
    if article.pic:
        try:
            print('process:' + article.pic)
            jpg_file = '/Users/user/work/python/sharejs' + article.pic
            im = Image.open(jpg_file)
            im.thumbnail( (250,179) )
            new_file = os.path.dirname(article.pic) + '/small_' + os.path.basename(article.pic)
            im.save('/Users/user/work/python/sharejs' + new_file)
            print "create small pic:" + new_file + ' finished'
            #article_facade.update_smallpic(article.id,new_file)
        except Exception:
            print(Exception)
