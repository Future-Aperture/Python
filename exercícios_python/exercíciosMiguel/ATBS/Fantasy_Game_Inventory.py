#Shows the inventory
def displayInventory(d):
    totalItems = 0

    # Display the items
    for k, v in d.items():
        print(f"{v}\t{k.title()}")
        totalItems += v

    # Display the total of items
    print(f"The total number of items is: {totalItems}")

#Adds items to the inventory
def addToInventory(inventory, listItems):
    for i in listItems:
        if i in inventory:
            inventory[i] += 1

        else:
            inventory.setdefault(i, 1)


inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventory(inv)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

addToInventory(inv, dragonLoot)

print()
displayInventory(inv)