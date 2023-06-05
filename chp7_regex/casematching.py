#CASE INSENSITIVE MATCHING
import re
#re.I & re.IGNORECASE mean the same thing. 
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())#Robocop
print(robocop.search('ROBOCOP protects the innocent.').group())#ROBOCOP
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())#robocop

print('\n-----\n')
#SUBBING STRINGS USING THE sub() METHOD
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))#CENSORED gave the secret documents to CENSORED.

print('\n-----\n')
agentNamesRegex = re.compile(r'Agent()')
print('\n---\n')
#phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?)(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext\x\ext.)\s*\d{2,5})?)')
phoneRegex = re.compile(r'((\d{3}|\d3\d3)?(\s|-|.)?\d{3}(\s|-|.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
print(phoneRegex)

#THIS IS HOW YOU PRINT IT
phoneRegex = re.compile(r'''(
    (\d{3}|(\d{3}\))?           #area code
    (\s|-|\.)?                  #separator
    \d{3}                       #first 3 digits
    (\s|-|\.)                   #separator
    (\d{4}                      #last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?    #extension
    )''', re.VERBOSE)