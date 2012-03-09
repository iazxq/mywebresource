# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

import simplejson
import os

from facade.admin import AdminFacade
from facade.book import BookFacade
from facade.booktag import BookTagFacade
from facade.bookindex import BookIndexFacade
from facade.bookchapter import BookChapterFacade

from views.accounts import adminuserinfo

from model.book import Book
from model.bookindex import  BookIndex,BookIndexKeyType
from model.bookchapter import BookChaper

from common import func
from common.pager import Pager

import settings


def book_list(request):
    '图书管理'
    sort = "id"
    start = func.get_int_param_from_get(request,'start')
    count = settings.DEFAULT_PAGE_SIZE
    book_facade = BookFacade()
    books = book_facade.search(sort=sort,start=start,count=count)
    book_list = books.get('list',[])
    total_count = books.get('total_count',0)
    pager = Pager(request,start,count,total_count)
    output = {
        'book_list':book_list,
        'pager':pager,
    }
    return render_to_response('admin/book_list.html',output)

def book_edit(request):
    '图书编辑'

    book_facade = BookFacade()

    #如果是提交信息
    if request.method =="POST":
        book = Book()
        id = func.get_int_param_from_post(request,'id')
        book.authors =  map(lambda x:x.strip(),request.POST.get('authors','').split('/'))
        book.translators = map(lambda x:x.strip(),request.POST.get('translators','').split('/'))
        book.authors_intro = request.POST.get('authors_intro','')
        book.binding = request.POST.get('binding','')
        book.dir = request.POST.get('dir','')
        book.spic = request.POST.get('spic','')
        book.mpic = request.POST.get('mpic','')
        book.bpic = request.POST.get('bpic','')
        book.isbn10 = request.POST.get('isbn10','')
        book.isbn13 = request.POST.get('isbn13','')
        book.pages = request.POST.get('pages','')
        book.price = request.POST.get('price','')
        book.pubdate = request.POST.get('pubdate','')
        book.publisher = request.POST.get('publisher','')
        book.summary = request.POST.get('summary','')
        book.title = request.POST.get('title','')
        book.sub_title = request.POST.get('sub_title','')
        book.tags = map(lambda x:x.strip(),request.POST.get('tags','').split('/'))


        #修改
        if id>0:
            book.id = id
            messages = book.validate()
            if not messages:
                book_facade.update(book)
                return_url = 'book_list'
                return HttpResponseRedirect(return_url)
            else:
                message=''
                if messages:
                    message = messages[0]
                output = {'message' :message}
                return render_to_response('admin/book_edit.html',output)
        else: #插入
            book.id = func.create_new_id()
            messages = book.validate()
            if not messages:
                book_facade.insert(book)
                return_url = 'book_list'
                return HttpResponseRedirect(return_url)
            else:
                message=''
                if messages:
                    message = messages[0]
                output = {'message' :message}
                return render_to_response('admin/book_edit.html',output)

    id = func.get_int_param_from_get(request,'id')
    output = {}

    if id>0:
        book = book_facade.get_data(id)
        output['book'] = book

    return render_to_response('admin/book_edit.html',output)

def book_del(request):
    '删除'
    id = int(request.GET.get('id',0))
    book_facade = BookFacade()
    book_facade.remove(id)
    return_url = func.get_referer(request,'book_list')
    return HttpResponseRedirect(return_url)

def pic_upload(request):
    from common import imagefactory
    file = request.FILES['pic']
    upload_path = func.get_new_upload_dir()
    save_path =  os.path.join(settings.ROOT_UPLOAD_DIR,upload_path).replace('\\','/')
    new_filename = func.get_new_filename(file.name)

    pic = new_filename
    spic = 's' + new_filename
    mpic = 'm' + new_filename
    bpic = 'b' + new_filename

    #return HttpResponse(str(file.size))
    #return HttpResponse(map(lambda x:x+'<br>',dir(file)))

    if not os.path.exists(save_path):
        os.makedirs(save_path)
    pic_file = os.path.join(save_path,pic).replace('\\','/')

    fd = open(pic_file, 'wb')
    fd.write(file.read())
    fd.close()

    spic_file = os.path.join(save_path,spic).replace('\\','/')
    mpic_file = os.path.join(save_path,mpic).replace('\\','/')
    bpic_file = os.path.join(save_path,bpic).replace('\\','/')

    upload_sucess = True
    upload_sucess &= imagefactory.create_small_pic(pic_file,settings.DEFAULT_SMALL_PIC_SIZE,spic_file)
    upload_sucess &= imagefactory.create_small_pic(pic_file,settings.DEFAULT_MIDDLE_PIC_SIZE,mpic_file)
    upload_sucess &= imagefactory.create_small_pic(pic_file,settings.DEFAULT_BIG_PIC_SIZE,bpic_file)

    # 格式 2011/08/2132132.jpg用于输出存储
    spic = os.path.join(upload_path,spic).replace('\\','/')
    mpic = os.path.join(upload_path,mpic).replace('\\','/')
    bpic = os.path.join(upload_path,bpic).replace('\\','/')

    result = {'spic':spic,'mpic':mpic,'bpic':bpic}
    return HttpResponse(simplejson.dumps(result))

def book_chapter_list(request):
    '章节管理'
    book_id = func.get_int_param_from_get(request,'book_id')
    book_chapter_facade = BookChapterFacade()
    book_facade = BookFacade();
    book = book_facade.get_data(book_id)
    book_chapters = book_chapter_facade.search(book_id)
    book_chapter_list = book_chapters['list']
    total_count = book_chapters['total_count']
    output = {
        'book':book,
        'book_chapter_list':book_chapter_list,
        'book_id':book_id,
    }
    return render_to_response('admin/book_chapter_list.html',output)

def book_chapter_edit(request):
    book_facade = BookFacade()
    book_chapter_facade = BookChapterFacade()
    id = func.get_int_param_from_get(request,'id')
    book_id = func.get_int_param_from_get(request,'book_id')
    book = book_facade.get_data(book_id)
    output = {'book_id':book_id,'book':book,}

    if request.method=="POST":
        book_chapter = BookChaper()
        book_chapter.book_id = func.get_int_param_from_post(request,'book_id')
        book_chapter.title = request.POST.get('title','')
        book_chapter.content = request.POST.get('content','')
        if id:#修改
            book_chapter.id = id
            messages = book_chapter.validate()
            if not messages:
                book_chapter_facade.update(book_chapter)
                return_url = 'book_chapter_list?book_id=%s'%book_chapter.book_id
                return HttpResponseRedirect(return_url)
            else:
                output['messages'] = messages
                return render_to_response('admin/book_chapter_edit.html',output)
        else:#插入
            book_chapter.id = func.create_new_id()
            messages = book_chapter.validate()
            if not messages:
                book_chapter_facade.insert(book_chapter)
                return_url = 'book_chapter_list?book_id=%s'%book_chapter.book_id
                return HttpResponseRedirect(return_url)
            else:
                output['messages'] = messages
                return render_to_response('admin/book_chapter_edit.html',output)

    #get 页面
    if id>0:
        book_chapter = book_chapter_facade.get_data(id)
        output['book_chapter'] = book_chapter

    return render_to_response('admin/book_chapter_edit.html',output)

def book_chapter_del(request):
    '删除'
    id = func.get_int_param_from_get(request,'id')
    book_chapter_facade = BookChapterFacade()
    book_chapter_facade.remove(id)
    return_url = func.get_referer(request,'book_chapter_list')
    return HttpResponseRedirect(return_url)


def test(reqeust):
    return render_to_response('admin/test.html')

if __name__ == "__main__":
    pass