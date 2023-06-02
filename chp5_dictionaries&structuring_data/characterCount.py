import pprint

message = 'I am the descendant of the last Mansa, Mansaba Janke Waali Sanneh. I have come to claim my title as the Mansabra.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)

'''
GOOD TO KNOW -- PPRINT FORMATS


pprint.pprint(someDictionaryValue)
print('\n')
pprint(pprint.pformat(someDictionaryValue))

'''