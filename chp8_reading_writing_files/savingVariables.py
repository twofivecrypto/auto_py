import shelve

shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('mydata')
type(shelfFile)
print(shelfFile['cats'])#['Zophie', 'Pooka', 'Simon']

#GETTING THE LIST FORM WITH list()
shelfFile = shelve.open('mydata')
print(list(shelfFile.keys()))#['cats']
print(list(shelfFile.values()))#[['Zophie', 'Pooka', 'Simon']]
shelfFile.close()