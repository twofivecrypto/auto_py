spam = '    Hello World     '
print(spam.strip()) # Hello World - removes all whitespace
print(spam.lstrip()) # Hello World     - strips white space on the left
print(spam.rstrip()) #    Hello World- strips white space on the right

spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS')) #BaconSpamEggs

