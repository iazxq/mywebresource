# -*- coding: utf-8 -*-
#自动添加类似的信息入库

import os

from facade import articlefacade
from facade import factory
from model.article import Article

#列表目录到数组
root_dir = r'D:\python\sharejs\vectors\d1'

dirs = os.listdir(root_dir)
print(dirs)

i=0;
#dirs =['blue', 'cantya', 'creative-media', 'green', 'happy-print-shop', 'indeziner-form-templates', 'one-page-cv', 'product-landing-page', 'sindromk', 'violet', 'write-to-santa']
for dir in dirs:
    i+=1
    if i<=100000:
        article = Article()
        article.title = u'矢量素材'
        article.short_description=u'矢量图格式为EPS，含JPG预览图，关键词:'
        article.compatibility = u''
        #article.demo_url = '/vectors/d1/%s/index.html'%dir
        article.root_category_id = 700
        article.category_id = 751
        article.full_download_url = '/vectors/d1/%s/%s.zip'%(dir,dir)
        article.pic = '/vectors/d1/%s/demo.jpg'%dir
        img_description = ''
        for file in os.listdir(root_dir + '\\' + dir):
            if file.endswith('.jpg') and file != 'demo.jpg':
                img_description += '[img]%s[/img]\r\n'%('/vectors/d1/'+dir+'/'+file)
        article.description = img_description
        #article.source = ''
        article_facade = factory.create_article_facade()
        article_facade.post_data(article)
        print(dir + '  finished')
