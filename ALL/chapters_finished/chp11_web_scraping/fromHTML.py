#! python3
# fromHTML.py -- we are creating a BeautifulSoup Object from HTML

import requests, bs4

res = requests.get('https://twofivecrypto.github.io/')
res.raise_for_status()
twoFiveCrypto = bs4.BeautifulSoup(res.text)
type(twoFiveCrypto)

#Loading an HTML file from hard drive.
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile)
type(exampleFile)