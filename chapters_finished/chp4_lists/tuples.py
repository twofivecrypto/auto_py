eggs = ('hello', 42, 0.5)
print(eggs[0])
print(eggs[1:3])
print(len(eggs))

print(type(('hello',)))
print(type(('hello')))

print('\n----------\n---------\n')
#CONVERTING A TUPLE TO A LIST IS HANDY IN CASE YOU NEED A MUTABLE VERSION OF A TUPLE VALUE

print(tuple(['cat', 'dog', 5]))
print(list(('cat', 'dog', 5)))
print(list('hello'))

spam = 42
cheese = spam
spam = 100
print(spam)
print(cheese)

#WHEN YOU ASSIGN A LIST TO A VARIABLE, YOU'RE ACTUALLY ASSIGING A LIST TO A REFERENCE OF THE VARIABLE -- POINTS TO A BIT OF DATA

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = 'Hello'
print(spam)
print(cheese)


