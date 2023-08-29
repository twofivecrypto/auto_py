print('Hello'.rjust(10)) #     Hello
print('Hello'.rjust(20)) #               Hello
print('Hello world!'.rjust(20)) #        Hello world!
print('Hello'.ljust(10)) #Hello     /5 empty spaces, a total of '10' spaces + 'hello': 5 + 5 = 10 characters

print('\nSpecify a fill character\n')

print('Hello'.rjust(20, '^')) #^^^^^^^^^^^^^^^Hello
print('Hello'.ljust(20, '$')) #Hello$$$$$$$$$$$$$$$

print('\nNow Let\'s .center() It\n')

print('Hello'.center(20)) #       Hello     /Hello is justified in the center of 20 characters in total
print('Hello'.center(20, '+')) #+++++++Hello++++++++


