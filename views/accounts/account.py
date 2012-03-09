# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

import repository
from common import func
from views.accounts import userinfo

#登录页面
def login(request,f="/"):
    '提交登录'
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user_repository = repository.user.UserRepository()
        user = user_repository.get_data(username=username)
        if user != None:
            response = HttpResponseRedirect(f)
            userinfo.set_cookie(response,user.id)
        else:
            message = "用户名或者密码不正确"
            response = render_to_response("accounts/login.html",{'message':message})
        return response
    
    return render_to_response("accounts/login.html")

def logout(request,f="/"):
    '登出'
    response = HttpResponseRedirect(f)
    userinfo.clear_cookie(response)
    return response

def register(request):
    '用户注册'
    user = User()
    
    if request.method == "POST":
        user.id = func.create_new_id()
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.nickname = request.POST.get('nickname')
        repassword = request.POST.get('repassword')

        messages = user.validate()

        if repassword != user.password:
            messages.insert(0,"两次输入的密码不一致")

        user_repository = repository.user.UserRepository()
        if user_repository.get_data(username=user.username) is not None:
            messages.append("邮箱已被使用，请更换")

        if user_repository.get_data(nickname=user.nickname) is not None:
            messages.append("昵称已被使用，请更换")

        if messages:
            message = messages[0]
            return render_to_response("accounts/register.html",locals())
        else:
            response = HttpResponseRedirect("thanks")
            userinfo.set_cookie(response,user.id)

            #保存用户信息到数据库
            user_repository.insert(user)
            return response
        
    return render_to_response("accounts/register.html",locals())


def thanks(request):
    return render_to_response("accounts/thanks.html")