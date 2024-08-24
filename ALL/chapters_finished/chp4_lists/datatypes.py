print([1,2,3])
print(['cat', 'bat', 'rat', 'elephant'])

spam = ['cat', 'rat', 'bat', 'whale']
print(spam)

print(spam[0])
print('hello ' + spam[1])

spam2 = [['cat', 'bat'], [10,20,30,40,50]]
print(spam2[0])
print(spam2[0][1])
print(spam2[1][4])
#NEGATIVE INDEXES
print(spam2[1][-3])
print(len(spam[0]))

spam[0] = 'aardvark'
print(len(spam[0]))

print(spam[0].title() * 3)
print(spam + ['a', 'b', 'c'])

del spam[0]
print(spam)
