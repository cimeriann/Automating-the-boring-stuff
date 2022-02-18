birthdays = {'dami': 'April the 5th'}
print(birthdays['dami'])
picnic_items = {'apples': 2, 'cups': 4}
print('I am bringing ' + str(picnic_items.get('mangoes', 0)) + ' apples')
picnic_items.setdefault('blankets', 5)
print(picnic_items)

# A simple tic tac toe game using dictionaries
theboard = { 'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' ' }

def printBoard(board):
    print(theboard['top-L'] + '|' + theboard['top-M'] + '|' + theboard['top-R'])
    print('-+-+-')
    print(theboard['mid-L'] + '|' + theboard['mid-M'] + '|' + theboard['mid-R'])
    print('-+-+-')
    print(theboard['low-L'] + '|' + theboard['low-M'] + '|' + theboard['low-R'])
printBoard(theboard)