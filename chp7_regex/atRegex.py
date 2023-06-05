import re

atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))#['cat', 'hat', 'sat', 'lat', 'mat']

print('\n-----\n')

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1))#Al
print(mo.group(2))#Sweigart
#BY DEFAULT USES GREEDY MODE, TO USE NONGREEDY MODE, SEE BELOW:
nonGreedyRegex = re.compile(r'<.*?>')
mo = nonGreedyRegex.search('<To serve man> for dinner.>')
print(mo)#<To serve man>
greedyRegex = re.compile(r'<.*>')
mo = greedyRegex.search('<To serve man> for dinner.>')
print(mo)#<To serve man> for dinner.>
print('\n--\n--')
#USING THE DOT CHARACTER
noNewlineregex = re.compile('.*')
print(noNewlineregex.search('''Serve the public trust.\n
                            Protect the innocent.\n
                            Serve the laws of God.''').group()) #Serve the public trust.

print('\n---\n---')
print('newline')