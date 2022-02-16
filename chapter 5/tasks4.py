birthdays = {'dami': 'April the 5th'}
print(birthdays['dami'])
picnic_items = {'apples': 2, 'cups': 4}
print('I am bringing ' + str(picnic_items.get('mangoes', 0)) + ' apples')
picnic_items.setdefault('blankets', 5)
print(picnic_items)