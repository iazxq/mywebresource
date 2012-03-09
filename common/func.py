# -*- coding: utf-8 -*-
import math,datetime,time,random,os

#与业务相关的函数

def get_rating_text(rating):
    '根据评价数字返回评价文本'
    rating_dict = {
        '1' : '很差',
        '2' : '较差',
        '3' : '还行',
        '4' : '推荐',
        '5' : '力荐',
    }
    return rating_dict.get(repr(rating))


#根据当前时间创建唯一编号
def create_new_id():
    d = datetime.datetime.now()
    return int(d.strftime("%Y%m%d%H%M%S") + str(d.microsecond/1000) + str(random.randint(10,99)))

def format_date(date_time):
    '格式化日期输出'
    return date_time.strftime('%Y-%m-%d')

def format_date_time(date_time):
    '格式化日期、时间输出'
    return date_time.strftime('%Y-%m-%d %H:%M:%S')

def str_to_datetime(str):
    '字符串转换成日期格式'
    try:
        format="%Y-%m-%d %H:%M:%S"
        return datetime.datetime.strptime(str,format)
    except:
        return datetime.datetime.now()


def get_int_param_from_post(request,param_name):
    '从request.POST获取整型参数'
    result = 0
    if param_name in request.POST:
        value = request.POST.get(param_name)
        if value.isdigit():
            result = int(value)
    return result

def get_int_param_from_get(request,param_name):
    '从request.GET获取整型参数'
    result = 0
    if param_name in request.GET:
        value = request.GET.get(param_name)
        if value.isdigit():
            result = int(value)
    return result

def get_str_param_from_post(request,param_name):
    '从request.POST获得字符串参数'
    return request.POST.get(param_name,'').encode('utf-8')

def get_str_param_from_get(request,param_name):
    '从request.GET获得字符串参数'
    return request.GET.get(param_name,'').encode('utf-8')

def get_referer(request,default_url=''):
    '返回引用页'
    return  request.META.get('HTTP_REFERER',default_url)

def get_new_upload_dir():
    '创建新的上传目录,返回格式/2011/08'
    d = datetime.datetime.now()
    return d.strftime('%Y/%m/')


def get_new_filename(filename):
    '返回新的文件名,利用Unix时间戳'
    f,ext=os.path.splitext(filename)
    return '%s%s'%(int(float(time.time()*1000)),ext)


def array_to_str(value,split_str='/'):
    '数组转换成'
    result = ''
    if value:
        for s in value:
            result += s + split_str
        result = result[:-1]
    return result

def format_content(str):
    return str.replace("\n","<br/>")








