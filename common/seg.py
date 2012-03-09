# -*- coding: utf-8 -*-

import smallseg
from base.globals import Globals

def cut(value):
    seg = Globals.get_seg()
    text = value.encode('utf8')
    result =  seg.cut(text)
    result = map(lambda x:x.lower(),result)
    return result


if __name__=="__main__":
    print(cut(u'hello world'))