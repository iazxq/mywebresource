# -*- coding: utf-8 -*-

import Image, ImageEnhance,os,sys,glob


def create_demo_pic(pic,new_width,new_height,out_file):
    im = Image.open(pic)
    pic_width,pic_height = im.size
    out_width = pic_width
    out_height = pic_height

    #按宽度缩放，其他的不管
    if pic_width > new_width:
        out_width = new_width
        out_height = int(float(pic_height * new_width) / pic_width)

    nim = im.resize((out_width,out_height),Image.BILINEAR)
    nim.save(out_file)

#创建demo.jpg 第一步
def create_demo_1():
    root_glob = r'D:\python\freecss\download\*'
    #glob 可以返回完整的路径
    for dir in glob.glob(root_glob):
        created = False
        try:
            for jpg_file in glob.glob('%s\*.jpg'%dir):
                if not jpg_file.endswith('demo.jpg'):
                    if not created:
                        create_demo_pic(jpg_file,460,310,dir+'\demo.jpg')
                        print('%s==>%s'%(jpg_file,dir+'\demo.jpg'))
                        created = True
        except Exception:
            print(Exception)


#把大的jpg图片统一缩小为600的宽度 第一步
def create_small_pic():
    root_glob = r'D:\python\freecss\download\*'
    #glob 可以返回完整的路径
    for dir in glob.glob(root_glob):
        try:
            for jpg_file in glob.glob('%s\*.jpg'%dir):
                    im = Image.open(jpg_file)
                    im.thumbnail( (600,600) )
                    im.save(jpg_file)
                    print('thumbnail jpg file : %s'%jpg_file)
        except Exception:
            print(Exception.message)


def create_last_demo_pic():
    root_glob = r'D:\python\freecss\download\*'
    #glob 可以返回完整的路径
    for dir in glob.glob(root_glob):
    #try:
        for jpg_file in glob.glob('%s\demo.jpg'%dir):
            im = Image.open(jpg_file)
            width,height=im.size
            if height>310:
                im=im.crop((0,(height-310)/2,width,(height-310)/2 + 310))
                im.save(jpg_file)
                print('create :' + jpg_file)
                #except Exception:
                #print(Exception.message)

if __name__=='__main__':
    create_demo_1()