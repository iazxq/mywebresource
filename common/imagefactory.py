# -*- coding: utf-8 -*-
import Image
import os

def create_small_pic(file,length,save_filename):
    '从文件创建小图片，图片按照length作为最大长度自由缩小'
    result = True

    #try:
    path,filename = os.path.split(save_filename)
    if not os.path.exists(path):
        os.makedirs(path)

    image = Image.open(file)
    image_width = image.size[0]
    image_height = image.size[1]

    if image_width <= length and image_height <= length:
        pass
    else:
        #如果宽大于高，则按照宽度缩小
        if image_width >= image_height:
            image_height = int(image_height * length / image_width)
            image_width = length
        else:
            #如果高大于宽，则按照高度缩小
            image_width = int(image_width * length / image_height)
            image_height = length

    image.thumbnail((image_width,image_height),Image.ANTIALIAS)
    image.save(save_filename,"jpeg")
    #except:
        #result = False
    return result
