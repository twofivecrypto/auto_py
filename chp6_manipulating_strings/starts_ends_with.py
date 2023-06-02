print('Hello world!'.startswith('Hello')) #True
print('Hello world!'.endswith('world!'))#True
print('abc123'.startswith('abcdef'))#False
print('abc123'.endswith('12'))#False
print('Hello world!'.startswith('Hello world!'))#True
print('Hello world!'.endswith('Hello world!'))#True
print('''\n\tThese methods are useful alternatives to the
                equals == operator if you need to check whether
                the first or last part of the string, rather than
                the whole thing, is equal to the string.''')

