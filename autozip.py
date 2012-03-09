# -*- coding: utf-8 -*-
'''
自动把文件夹下的所有子文件夹打包成zip
'''


import zipfile,os

root_dir = r'D:\python\freecss\download'
#列出全部文件夹
dirs = os.listdir(root_dir)

for d in dirs:
    zip = zipfile.ZipFile('%s.zip'%d,'w',zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(root_dir + os.sep + d):
        for filename in filenames:
            if not filename in ('demo.jpg'):
                file_path = os.path.join(dirpath, filename)
                rel_file_path = os.path.join(root_dir,d)
                #relpath 表示从root_dir 开始计算路径
                zip.write(file_path,os.path.relpath(file_path,rel_file_path))
    zip.close()
    os.system('copy %s.zip %s.zip'%(d,root_dir+os.sep+d+os.sep+d))
    os.system('del %s.zip'%d)
    print('%s 完成'%d)