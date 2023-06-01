def lb():
    print('-----')

spam = ['hello', 'hi', 'howdy', 'heyas', 'hi']
print(spam.index('hello'))
lb()
print(spam.index('heyas'))
lb()
print(spam.index('hi'))
lb()

#WHEN DUPLICATE VALUES ARE IN A LIST, FIRST INSTANCE IS RETURNED
print(spam.index('hi'))

#ADDING VALUES WITH APPEND & INSERT
spam = ['hello', 'hi', 'howdy', 'heyas', 'hi']
spam.append('waddup')
print(spam)

spam.insert(0, 'world')
print(spam)

spam.remove('howdy')
print(spam)

spam.sort()
print(spam)


#USES ASCIIbetical order, WHICH MEANS 'Z' comes before 'a'. 

