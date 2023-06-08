import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
print(shelfFile.close())

shelfFile - shelve.open('mydata')
type(shelfFile)
print(shelfFile['cats'])