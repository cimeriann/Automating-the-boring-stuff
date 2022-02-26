# Table Printer
# Write a function named printTable() that takes a list of lists of strings 
# and displays it in a well-organized table with each column right-justified. 
# Assume that all the inner lists will contain the same number of strings. 
# For example, the value could look like this:
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(list):
    
    for i in list:
        print((' ').join(i))

printTable(tableData)