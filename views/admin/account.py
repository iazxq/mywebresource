# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from views.accounts import adminuserinfo
from repository.admin import AdminRepository

def login(request):
    '登录页面'

    if adminuserinfo.is_login(request):
        return HttpResponseRedirect('/admin')

    msg = ''
    username = ''

    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        admin_repository = AdminRepository()
        if admin_repository.login(username,password):
            adminuserinfo.set_session(request,username)
            return HttpResponseRedirect('/admin')
        else:
            msg = '用户名或者密码不正确'

    output = {
        'username':username,
        'msg' : msg,
    }

    return render_to_response('admin/login.html',output)


def logout(request):
    adminuserinfo.logout(request)
    return HttpResponseRedirect('login')


def check_login(func):
    '''
    声明一个检查登录的装饰器
    '''
    def check(request,*args, **args2):
        if adminuserinfo.is_login(request):
            return func(request,*args,**args2)
        else:
            return HttpResponseRedirect('login')
    return check