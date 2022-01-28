#A function is like a mini-function inside a program
# # Write a function named collatz() that has one parameter named number. If 
# number is even, then collatz() should print number // 2 and return this value. 
# If number is odd, then collatz() should print and return 3 * number + 1.
# Then write a program that lets the user type in an integer and that keeps 
# calling collatz() on that number until the function returns the value 1

# from ast import Num


def collatz(number):
    if number % 2 == 0:
        return number // 2
        
    elif number % 2 ==1:
        return number * 3 + 1
while True:
    try:
        yinka = int(input('Input a number: '))
        print(collatz(yinka))
        if collatz(yinka) != 1:
            continue
        elif yinka == int:
            print('please input an integer')
            
        else:
            break
    except:
        print('Please enter an integer.')

       