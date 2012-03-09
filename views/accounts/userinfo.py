# -*- coding: utf-8 -*-

#用户Cookie信息
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import base.config
import repository



def set_cookie(response,user_id):
    #设置Cookie
    response.set_cookie(key="user_id", value=user_id, max_age=365*24*60*60,secure=False)

def clear_cookie(response):
    '清除cookie'
    response.delete_cookie("user_id")

def is_login(request):
    #判断Cookie是否已经存在
    user_id = get_user_id(request)
    if user_id > 0:
        return True
    else:
        return False
    
def get_cookie(request,key):
    #获取cookie
    return request.COOKIES.get(key)

def get_user_id(request):
    #从Cookie获取用户编号
    user_id = str(get_cookie(request,"user_id"))
    if user_id.isdigit():
        return int(user_id)
    else:
        return 0

def get_user(request):
    '从cookie获取用户信息返回'
    user_id = get_user_id(request)
    if user_id>0:
        user_repository = repository.user.UserRepository()
        user = user_repository.get_data(id=user_id)
        return user
    else:
        return None
    



