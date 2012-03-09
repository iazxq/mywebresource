# -*- coding: utf-8 -*-
import repository
import settings

def set_session(request,username):
    request.session['admin'] = username

def get_session(request):
    return request.session.get('admin',None)

def is_login(request):
    '判断用户是否已经登录'
    session =  get_session(request)
    return session is not None

def logout(request):
    request.session['admin'] = None