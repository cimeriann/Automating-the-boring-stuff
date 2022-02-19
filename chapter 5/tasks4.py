# display inventory code
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

# add to inventory code
# dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# def add_to_inventory(some_inventory, list_of_items):

    


    
