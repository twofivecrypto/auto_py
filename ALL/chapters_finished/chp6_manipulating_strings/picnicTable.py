def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))
picnicItems = {
    'sandwiches': 4,
    'apples': 12,
    'cups': 4,
    'cookies': 8000
}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
printPicnic(picnicItems, 40, 12)

'''
OUTPUT BELOW: PRINTS picnicItems, centered, then the keys to left width + padding with dots
                and then prints the values with right width + padding with spaces
                    NOTE --- the integers represent the column spacing
---PICNIC ITEMS--
sandwiches..    4
apples......   12
cups........    4
cookies..... 8000
-------PICNIC ITEMS-------
sandwiches..........     4
apples..............    12
cups................     4
cookies.............  8000
--------------------PICNIC ITEMS--------------------
sandwiches..............................           4
apples..................................          12
cups....................................           4
cookies.................................        8000
'''