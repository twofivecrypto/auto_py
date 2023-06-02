displayInventory = {
    'arrow': 12,
    'gold coin': 42,
    'rope': 1,
    'torch': 6,
    'dagger': 1
}

def totalInventory(tools, count):
    return tools.get(count, 0)


print('Inventory:\n')
print(str(totalInventory(displayInventory, 'arrow')) + ' arrows')
print(str(totalInventory(displayInventory, 'gold coin')) + ' gold coins')
print(str(totalInventory(displayInventory, 'rope')) + ' rope coins')
print(str(totalInventory(displayInventory, 'torch')) + ' torch')
print(str(totalInventory(displayInventory, 'dagger')) + ' dagger')

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1

addToInventory(displayInventory, dragonLoot)
for item, count in displayInventory.items():
    print(f"{count} {item}")

'''
Step 1:
We start with a dictionary called displayInventory which represents the initial inventory of items. Each item is paired with a count.

Step 2:
There is a function called totalInventory that takes two arguments: tools (the inventory dictionary) and count (the specific item we want to count). This function retrieves the count of the specified item from the inventory dictionary using the get() method.

Step 3:
We print a heading "Inventory:" to indicate that we are going to display the current inventory.

Step 4:
We use the totalInventory function to get the count of different items from the displayInventory dictionary, and we print the counts alongside their corresponding item names.

Step 5:
We define a list called dragonLoot which contains additional items that need to be added to the inventory.

Step 6:
There is a function called addToInventory that takes two arguments: inventory (the inventory dictionary) and addedItems (the list of items to be added). Inside this function, we iterate over each item in the addedItems list.

Step 7:
For each item in the addedItems list, we update the count of that item in the inventory dictionary. If the item already exists in the dictionary, we increment its count by 1. If the item doesn't exist, we add it to the dictionary with a count of 1 using the get() method.

Step 8:
We call the addToInventory function to add the items from the dragonLoot list to the displayInventory dictionary.

Step 9:
We print a heading "Updated Inventory:" to indicate that we are going to display the updated inventory.

Step 10:
We loop through each item and its count in the displayInventory dictionary, and we print the count followed by the item name.

By following these steps, the code displays the initial inventory, adds the items from dragonLoot to the inventory, and then shows the updated inventory with the counts of each item.
'''