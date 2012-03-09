# -*- coding: utf-8 -*-
import Image, ImageEnhance,os,sys

def reduce_opacity(im, opacity):
    """Returns an image with reduced opacity."""
    assert opacity >= 0 and opacity <= 1
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    else:
        im = im.copy()
    alpha = im.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    im.putalpha(alpha)
    return im

def watermark(im, mark, position, opacity=1):
    """Adds a watermark to an image."""
    if opacity < 1:
        mark = reduce_opacity(mark, opacity)
    if im.mode != 'RGBA':
        im = im.convert('RGBA')
        # create a transparent layer the size of the image and draw the
    # watermark in that layer.
    layer = Image.new('RGBA', im.size, (0,0,0,0))
    if position == 'tile':
        for y in range(0, im.size[1], mark.size[1]):
            for x in range(0, im.size[0], mark.size[0]):
                layer.paste(mark, (x, y))
    elif position == 'scale':
        # scale, but preserve the aspect ratio
        ratio = min(
            float(im.size[0]) / mark.size[0], float(im.size[1]) / mark.size[1])
        w = int(mark.size[0] * ratio)
        h = int(mark.size[1] * ratio)
        mark = mark.resize((w, h))
        layer.paste(mark, ((im.size[0] - w) / 2, (im.size[1] - h) / 2))
    else:
        layer.paste(mark, position)
        # composite the watermark with the layer
    return Image.composite(layer, im, layer)

def add_water():
    root_dir = r'D:\python\freecss\download'
    dirs = os.listdir(root_dir)

    i=0

    for dir in dirs:
        try:
            dir = root_dir+os.sep + dir
            #os.system(r'web2pic.exe %s\index.html %s\demo.jpg'%(dir,dir))

            im = Image.open("%s\demo.jpg"%dir)
            mark = Image.open('www.sharejs.com2.png')
            #watermark(im, mark, 'tile', 0.5)
            #watermark(im, mark, 'scale', 1.0)
            im_width,im_height = im.size
            mark_width,mark_height = mark.size

            position = (im_width-mark_width-10,im_height-mark_height-10)
            watermark(im, mark, position, 1).save('%s\demo.jpg'%dir)
            i += 1
            print('%s.%s finished'%(i,dir))
        except Exception:
            print(Exception.message)

def test():
    im = Image.open('c:\\1.eps')
    im.save('c:\\1.jpg','JPG')



if __name__ == '__main__':
    add_water()
    #test()