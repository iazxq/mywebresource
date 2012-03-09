# -*- coding: utf-8 -*-
"""This is a copy of the htmlEncode function in Webware.


@@TR: It implemented more efficiently.

"""
htmlCodes = [
    ['&', '&amp;'],
    ['<', '&lt;'],
    ['>', '&gt;'],
    ['"', '&quot;'],
]
htmlCodesReversed = htmlCodes[:]
htmlCodesReversed.reverse()

def html_decode(s, codes=htmlCodes):
    """ Returns the HTML encoded version of the given string. This is useful to
    display a plain ASCII text string on a web page."""
    for code in codes:
        s = s.replace(code[1], code[0])
    return s

def html_encode(s, codes=htmlCodes):
    for code in codes:
        s = s.replace(code[0], code[1])
    return s