spam = 'hello world'

print(spam.upper())
print(spam.lower())

bacon = 'Hello girl'
print(bacon.upper())
print(bacon.islower())
print(bacon.isupper())
print('HELLO'.isupper())
print('hello'.isupper())

print('Hello'.upper())
print('Hello'.upper().lower())
print('Hello'.upper().lower().upper())
print('Hello'.lower())
print('Hello'.lower().islower())#TRUE
print('\n')
print('Hello'.lower().isupper())#FALSE

print('hello'.isalpha())#TRUE
print('helo123'.isalpha())#FALSE
print('hello123'.isalnum())#TRUE
print('hello'.isalnum())#TRUE
print('123'.isdecimal())#TRUE
print(' '.isspace())#TRUE
print('This Is Title Case'.istitle())#TRUE
print('This Is Title Case 123'.istitle())#TRUE
print('THIS Is not Title Case'.istitle())#FALSE
print('This Is NOT Title Case Either'.istitle())#FALSE
