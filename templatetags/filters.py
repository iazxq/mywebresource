# -*- coding: utf-8 -*-
from django.template import Library
from common import ubb
from common import func

register = Library()


def left_str(value,length):
    '从左边截取指定长度的字符串，一个中文算两个字符'

    try:
        value = value.decode('utf-8')
    except:
        pass

    if length <=0:
        return value

    result = ''

    value_byte_length = len(value.encode('GB18030'))

    # 如果编码后的字符串的长度还不到指定长度，则直接返回
    if value_byte_length<=length :
        return value



    cut_len = 0 #记录已截取长度
    for c in value:
        cut_len += len(c.encode('GB18030'))
        if cut_len <= length:
            result += c

    if len(result) < length :
        result += "..."

    return result
register.filter(left_str)


def file_path(value):
    '反问文件相对路径'
    return '/up/%s'%value
register.filter(file_path)


def array_to_str(value,split_str='/'):
    '数组转换成字符串'
    return func.array_to_str(value,split_str)
register.filter(array_to_str)

def rating_to_star(value):
    '把平均得分转换成星星，例如10分=长度为50的星星'
    if not value:
        return 0
    return int(round(value * 5 /5,0) *5)
register.filter(rating_to_star)


def format_content(value):
    '格式化内容显示，替换换行符等'
    return value.replace("\n","<br/>").replace(" ","&nbsp")
register.filter(format_content)


def format_date(date_time):
    '格式化日期输出'
    return date_time.strftime('%Y-%m-%d')
register.filter(format_date)

def format_date_time(date_time):
    '格式化日期时间输出'
    return func.format_date_time(date_time)
register.filter(format_date_time)

def ubb_to_html(content):
    return ubb.ubb_to_html(content)
register.filter(ubb_to_html)

def get_state(state):
    state_dict = {0:'<font color=red>隐藏</font>',
                  1:'显示'}
    return state_dict.get(state,'未知')
register.filter(get_state)

if __name__ == "__main__":
    print(left_str(u'aab我们都是害虫333',12))