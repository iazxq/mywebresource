# -*- coding: utf-8 -*-
'''
批量重命名
'''

import os

root_dir = r'D:\python\freecss\download'


def rename_dirs():
    dirs = os.listdir(root_dir)
    i=10000
    for dir in dirs:
        try:
            i+=1
            #批量重命名文件夹
            #os.rename(root_dir + os.sep + dir,'%s%s%s'%(root_dir,os.sep,str(i)))

            #批量重命名所有文件


        except Exception:
            print("%s rename error"%Exception.message)

'''
def rename_files():
    dirs = os.listdir(root_dir)
    for d in dirs:
        for dirpath, dirnames, filenames in os.walk(root_dir + os.sep + d):
            for filename in filenames:
                f = dirpath + os.sep + filename
                if f.find('_lanrentuku.com')>=0:
                    print(f)
                    try:
                        os.rename(f,f.replace('_lanrentuku.com',''))
                        #print(f)
                    except Exception:
                        print(Exception.message)

'''

def copy_files():
    '''
    批量把子目录下的文件移出来
    '''
    dirs = os.listdir(root_dir)
    for dir in dirs:
        #检查是否存在子文件夹
        for d in os.listdir(root_dir + os.sep + dir):
            if os.path.isdir(root_dir+os.sep+dir+os.sep+d):
                print('copy %s %s'%(root_dir+os.sep+dir+os.sep+d+os.sep+'*.*',root_dir+os.sep+dir+os.sep))
                os.system('copy %s %s'%(root_dir+os.sep+dir+os.sep+d+os.sep+'*.*',root_dir+os.sep+dir+os.sep))
                os.system('del %s'%root_dir+os.sep+dir+os.sep+d+os.sep+'*.*')
                os.removedirs(root_dir+os.sep+dir+os.sep+d)

def rename_files():
    dirs = os.listdir(root_dir)

    for dir in dirs:
        current_dir = root_dir + os.sep + dir
        i=1000
        deleted=False
        for d in os.listdir(current_dir):
            ext = d.split('.')[-1]
            if ext in ('cdr') and not deleted:
               os.system('rd /S /Q %s'%current_dir)
               deleted = True
               #i+=1
               #os.rename(current_dir+os.sep+d,current_dir+os.sep + 'sharejs_com_'+str(i) + '.' + ext)
               print(current_dir+os.sep + 'sharejs_com_'+str(i) + '.'+ ext)


#为eps创建jpg图片
def create_pic():
    dirs = os.listdir(root_dir)
    for dir in dirs:
        if int(dir)>0:
            current_dir = root_dir + os.sep + dir
            #print('current dir:%s'%current_dir)
            for d in os.listdir(current_dir):
                ext = d.split('.')[-1]
                if ext in ('cdr'):
                    current_file = current_dir + os.sep + d
                    os.system('gswin32c -q -dBATCH -dEPSCrop -sDEVICE=jpeg -r300   -dNOPAUSE -dSAFER -sOutputFile=%s %s'%(current_file+'.jpg',current_file))
                    print('outFile=%s %s'%(current_file+'.jpg',current_file))

if __name__== '__main__':
    rename_files()
    #copy_files()
    #create_pic()
    #rename_files()
    
    
