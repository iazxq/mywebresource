# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

import account

@account.check_login
def index(request):
    '后台主页'
    return render_to_response('admin/index.html')
