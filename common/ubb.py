# -*- coding: utf-8 -*-
import re
import urllib2
from common.html import html_decode,html_encode
def ubb_to_html(content):


    p = re.compile('<',re.IGNORECASE)
    content = p.sub(r'&lt;',content)

    p = re.compile('>',re.IGNORECASE)
    content = p.sub(r'&gt;',content)


    p = re.compile('\n',re.IGNORECASE)
    content = p.sub(r'<br/>',content)

    p = re.compile('<br/><br/>',re.IGNORECASE)
    content = p.sub(r'<br/>',content)



    #[b][/b]
    p = re.compile('\[b\]([ \S\t]*?)\[\/b\]',re.IGNORECASE)
    content = p.sub(r'<b>\1</b>',content)

    #[img][/img]
    p = re.compile('\[IMG\]([\s\S]+?)\[/IMG\]',re.IGNORECASE)
    content = p.sub(r'<img src="\1" border="0" />',content)

    #[url]http://www.sharejs.com[/url]
    p = re.compile('\[url\]([ \S\t]*?)\[/url\]',re.IGNORECASE)
    content = p.sub(r'<a href="\1" target="_blank">\1</a>',content)

    #[url=http://www.sharejs.com]JavaScript[/url]
    p = re.compile('\[url=([ \S\t]+?)\]([ \S\t]*?)\[/url\]',re.IGNORECASE)
    content = p.sub(r'<a href="\1" target="_blank">\2</a>',content)

    #[color=][/color]
    p = re.compile('\[color=([\S]+)\]([ \S\t]*?)\[/color\]',re.IGNORECASE)
    content = p.sub(r'<font color="\1">\2</font>',content)

    #[runcode][/runcode]
    p = re.compile('\[runcode\]([\S\s]*?)\[/runcode\]',re.IGNORECASE)
    content = p.sub(lambda x:html_decode(x.group(1).replace('<br/>','\n')),content)

    #[code][/code]
    p = re.compile('\[code\]([\S\s]*?)\[/code\]',re.IGNORECASE)
    content = p.sub(lambda x: '<pre class="prettyprint html linenums">%s</pre>'%x.group(1).replace(r'<br/>','\n'),content)

    #[codebox][codebox]
    p = re.compile('\[codebox\]([\s\S]*?)\[/codebox\]',re.IGNORECASE)
    content = p.sub(lambda x: '<pre class="prettyprint html linenums">%s</pre>'%x.group(1).replace(r'<br/>','\n'),content)

    #[runtimecode][/runtimecode]
    p = re.compile('\[runtimecode\]([\s\S]*?)\[/runtimecode\]',re.IGNORECASE)
    content = p.sub(lambda x: '<pre class="prettyprint html linenums">%s</pre>'%x.group(1).replace(r'<br/>','\n'),content)

    '''
    #[runtimecode][/runtimecode]
    p = re.compile('\[runtimecode\]([\s\S]*?)\[/runtimecode\]',re.IGNORECASE)
    content = p.sub(lambda x:html_decode(x.group(1)),content)
    '''

    #[copyright][/copyright]
    p = re.compile('\[copyright\]([\s\S]*?)\[/copyright\]',re.IGNORECASE)
    content = p.sub(ur'''
        /*****************************************************
         *  Share JavaScript (http://www.ShareJS.com)
         * 使用此脚本程序，请保留此声明
         * 获取此脚本以及更多的JavaScript程序，请访问 http://www.ShareJS.com
         ******************************************************/
    ''',content)

    return content


if __name__=='__main__':
    print(ubb_to_html('''i love [b]hello world[/b],and you?
                      shide
                      [ img][ /img]:[img]http://www.sharejs.com/images/logo.gif[/img]
                      [ url][ /url]:[url]http://www.sharejs.com[/url]
                      [ url=xxx]xxx[ /url]:[url=http://www.bandao.cn]hello[/url]
                      [ color=#red][ /color]:[color=#red]red color[/color]
                      [ copyright][ /copyright]:[copyright]jQuery[/copyright]
                      '''))
