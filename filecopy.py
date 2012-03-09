# -*- coding: utf-8 -*-
'''
自动拷贝指定的文件到所有的文件夹
'''
__author__ = 'Administrator'

import os

source = 'C:\\Users\\Administrator\\Desktop\\sharejs\\about\\*.*'
target_dir = 'D:\\python\\freecss\\download\\'

dirs = os.listdir(target_dir)
for dir in dirs:
    copy_command = 'copy %s %s%s\\'%(source,target_dir,dir)
    os.system(copy_command)
