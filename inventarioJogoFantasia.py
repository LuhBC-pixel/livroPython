inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inventory):
    print("Inventory:")
    totalItem = 0

    for k, v in inventory.items():
        print(str(v), k)
        totalItem += v

    print(f'Total number of items: {str(totalItem)}')

def addToInventory(inventory, addedItems):
    for items in addedItems:
        inventory.setdefault(items, 0)
        inventory[items] = inventory[items] + 1

    return inventory

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)