# -*- coding: utf-8 -*-
import re

def check_len(value,min,max):
    '检查字符串的长度是否在min-max之间'

    #先将utf8编码转换成unicode，然后转换成gbk，gbk在使用
    length = len(value.encode('gbk'))
    if min <= length <= max:
        return True
    else:
        return False


def is_email(str):
    '检查给定的字符串是否是Email'

    #如果邮件长度不是4-50个字符，则认为不正确
    if not check_len(str,4,50):
        return False

    pattern = r"^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$"
    m = re.match(pattern,str)
    return m is not None

def is_valid_password(str):
    '判断是否是可用的密码'

    #密码长度范围是4-20个字符
    if not check_len(str,4,20):
        return False

    pattern = r"^\w+$"
    m = re.match(pattern,str)
    return m is not None

def is_valid_nickname(str):
    '判断是否是可用的昵称'
    if not check_len(str,4,14):
        return False

    pattern = ur"^[-_a-zA-Z0-9\u4e00-\u9fa5]+$"
    m = re.match(pattern,str)
    return m is not None


if __name__ == "__main__":
    #print(is_email('iazxq@sohu.com333 hhdye'))
    #print(is_valid_password('3213g_23iu38'))
    #print(is_valid_nickname('不吃皮蛋吃鸡蛋'))
    print(check_len('不吃皮单吃',4,14))
