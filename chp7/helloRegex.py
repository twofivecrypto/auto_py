import re

beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!')) # <sre.SRE_Match object; span=(0,5), match='Hello'>
print(beginsWithHello.search('He said hello')) # None

