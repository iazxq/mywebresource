# -*- coding: utf-8 -*-
'''
批量重命名
'''

import os

root_dir = r'D:\python\sharejs\temp\free-css-templates.com'

dirs = os.listdir(root_dir)

for dir in dirs:
    os.rename(root_dir + os.sep + dir,root_dir+os.sep+dir.lower().replace('-','_'))


