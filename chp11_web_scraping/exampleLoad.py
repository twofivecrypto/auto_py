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

pElems = exampleSoup.select('p')
if len(pElems) > 0:
    print(str(pElems[0]))
    print(pElems[0].getText())
    if len(pElems) > 1:
        print(str(pElems[1]))
        print(pElems[1].getText())
    if len(pElems) > 2:
        print(str(pElems[2]))
        print(pElems[2].getText())