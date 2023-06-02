'''birthdays = {
    'famara': 'Nov 9',
    'modou': 'Feb 15',
    'sanna': 'Apr 3',
    'sally': 'May 8'
}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthdday ')
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
print(birthdays)
'''
def linebreak():
    print('\n----\n')
print('\n\n\n')

spam = {
    'color': 'red',
    'age': 42
}
for v in spam.values():
    print(v)

linebreak()

print(spam.keys())

linebreak()

print(list(spam.keys()))

linebreak()

for k, v in spam.items():
    print('Key: ' + k + 'Value: ' + str(v))

linebreak()

spam = {'name': 'Famara', 'age': '28'}
for name in spam.keys():
    print(name)

for v in spam.values():
    print(v)


#THE 'get()' METHOD
picnicItems = {
    'apples': 5,
    'cups': 2
}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

#THE setdefault() METHOD
player = {
    'name': 'famara',
    'age': 28
}
print(player)
if 'rank' not in player:
    player['rank'] = 'mansa'
print(player)
#now do it in one line of code
player.setdefault('country', 'the gambia')
print(player)

