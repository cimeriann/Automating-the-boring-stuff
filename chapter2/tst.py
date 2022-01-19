# def spam():
    
#     global eggs
#     print(eggs)

# eggs = 'bagel'
# def bacon():
#     eggs = 'bacon'
#     print(eggs)

# spam()
# bacon()

# def spam(divideby):
#     try:
#         return 42/ divideby
#     except ZeroDivisionError:
#         print('Error Invalid Operation.')

# print(spam(3))
# print(spam(4))
# print(spam(0))

#This is a guess the number game
# import random
# secretnumber = random.randint(1,20)
# print('I am thinking of a number between 1 and 20')
# for numofguesses in range(1,7):
#     guess = int(input('Take a guess: '))

#     if guess > secretnumber:
#         print('Your guess is too high')
#     elif guess < secretnumber:
#         print('Your guess is too low')
#     else:
#         break
# if guess == secretnumber:
#     print('Good job! You guessed my number in ' + str(numofguesses) + ' guesses!')
# else:
#     print('Nope! my secret number is ' + str(secretnumber))
#     print('Nope. The number I was thinking of was ' + str(secretnumber))
    
def addnum(x,y):
    return x+y
    

addnum(5,1827377)