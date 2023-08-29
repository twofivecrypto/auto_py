print(', '.join(['cats', 'rats', 'bats'])) #cats, rats, bats
print(' '.join(['My', 'name', 'is', 'Pa', 'Famara', 'Sanneh'])) #My name is Pa Famara Sanneh
print('ABC'.join(['My', 'name', 'is', 'Pa', 'Famara', 'Sanneh'])) #MyABCnameABCisABCPaABCFamaraABCSanneh
def linebreak():
    print('\n-----------\n')

print('My name is Pa Famara Sanneh'.split()) #['My', 'name', 'is', 'Pa', 'Famara', 'Sanneh']
print('MyABCnameABCisABCPaABCFamaraABCSanneh'.split('ABC'))#['My', 'name', 'is', 'Pa', 'Famara', 'Sanneh']
print('My name is Pa Famara Sanneh'.split('a'))#['My n', 'me is P', ' F', 'm', 'r', ' S', 'nneh']

linebreak()

spam = '''Dear Alice,
How have you been? I am fine.
There is a container in the fridge
that is labeled "Milk Experiment".

Please do not drink it.
Sincerely,
Mansa'''
print(spam.split('\n')) #['Dear Alice,', 'How have you been? I am fine.', 'There is a container in the fridge', 'that is labeled "Milk Experiment".', '', 'Please do not drink it.', 'Sincerely,', 'Mansa']




