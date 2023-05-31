print('\t\ncontinue Statements')

while True:
    print('Who are you?')
    name = input()
    if name != 'Famara':
        continue
    print('Hello, Famara. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')