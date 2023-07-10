#! python3
# exampleLoad.py -- practicing using tags with beautiful soup and an .html file from the hard drive

import bs4

exampleFile = open("D:\\auto_py\\chp9_organizing_files\\index.html")
exampleSoup = bs4.BeautifulSoup(exampleFile.read(), features="html.parser")
elems = exampleSoup.select('#author')
print(type(elems))
print(len(elems))
if len(elems) > 0:
    print(type(elems[0]))
    print(elems[0].getText())
    print(str(elems[0]))
    print(elems[0].attrs)

