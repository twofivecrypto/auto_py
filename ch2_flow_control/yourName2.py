'''name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
    break
print('Thank you!')
'''

name = ''
while not name:
    print('Enter your name')
    name = input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests:
    print('Be sure to have enough room for your guests.')
print('Done')

