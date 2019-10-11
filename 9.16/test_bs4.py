#-*-coding:utf-8-*-

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

#创建 Beautiful Soup 对象
soup = BeautifulSoup(html,'lxml')

print(soup.title)
# <title>The Dormouse's story</title>

print (soup.head)
# <head><title>The Dormouse's story</title></head>

print (soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>

print (soup.p)
# <p class="title" name="dromouse"><b>The Dormouse's story</b></p>

print (type(soup.p))
# <class 'bs4.element.Tag'>