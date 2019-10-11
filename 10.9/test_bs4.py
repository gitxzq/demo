from bs4 import BeautifulSoup
html="""
<html><head><title> the dormouse's story </title></head>
<body>
<p class="title" name="dormouse"><b>the dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup=BeautifulSoup(html,'lxml')

print(soup.title) 
#<title> the dormouse's story </title>


print(soup.head)
# <head><title> the dormouse's story </title></head>

print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>

print(soup.p)

# <p class="title" name="dormouse"><b>the dormouse's story</b></p>

print(type(soup.p))
# <class 'bs4.element.Tag'>

print(soup.name)
# [document]

print(soup.head.name)
# head

print(soup.p.attrs)
# {'class': ['title'], 'name': 'dormouse'}

print(soup.p['class'])
# ['title']

soup.p['class']="newClass"
print(soup.p)
# <p class="newClass" name="dormouse"><b>the dormouse's story</b></p>

print(soup.title.string)