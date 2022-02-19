inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def display_inventory(some_inventory):
    print('Inventory: ')
    for k,v in some_inventory.items():
        print(str(v)+ ' ' + k)
    total = 0
    for k,v in some_inventory.items():
        total += v

    print('Total number of items: ' + str(total))

display_inventory(inventory)


    
