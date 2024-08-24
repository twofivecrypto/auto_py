#! python3
# exampleData.py -- practicing using tags with beautiful soup and an .html file from the hard drive

import bs4

soup = bs4.BeautifulSoup(open('example.html'))
spanElem = soup.select('span')[0]
print(str(spanElem))
print(spanElem.get('id'))
print(spanElem.get('some_nonexistent_addr') == None)
print(spanElem.attrs)