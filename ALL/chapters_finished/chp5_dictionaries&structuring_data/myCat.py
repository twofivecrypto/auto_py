myCat = {
    'size': 'fat',
    'color': 'gray',
    'disposition': 'loud'
}

print(myCat['size'])
print('My cat has ' + myCat['color'] + ' fur.')

#DICTIONARIES CAN STILL USE INTEGER VALUES AS KEYS, BUT DON'T HAVE TO START AT 0 AND CAN BE ANY NUMBER

print('\n\n')

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon) # FALSE

eggs = {
    'name': 'Zophie',
    'species': 'cat',
    'age': '8'
}
ham = {
    'species': 'cat',
    'name': 'Zophie',
    'age': '8'
}
print(eggs == ham)#TRUE
#DICTIONARIES CAN'T BE SLICED LIKE LISTS BECAUSE THEY'RE UNORDERED

