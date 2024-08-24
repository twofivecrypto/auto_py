allGuests = {
    'Famara': {'mangos': 9, 'strawberries': 12},
    'Bistro': {'apples': 8, 'oranges': 5},
    'H0ly': {'lemons': 3, 'bananas': 7}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought

print('Number of fruits being brought:')
print(' - Mangos        ' + str(totalBrought(allGuests, 'mangos')))
print(' - Strawberries        ' + str(totalBrought(allGuests, 'strawberries')))
print(' - Apples        ' + str(totalBrought(allGuests, 'apples')))
print(' - Oranges        ' + str(totalBrought(allGuests, 'oranges')))
print(' - Lemons        ' + str(totalBrought(allGuests, 'lemons')))
print(' - Bananas        ' + str(totalBrought(allGuests, 'bananas')))

