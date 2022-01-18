#Question 8:Identify the three indented blocks
spam = 0
if spam == 10:
    print('eggs') #block 1
    if spam > 5:
        print('bacon') #block 2
    else:
        print('ham') #block 3


print('spam')
print('spam')
#the indented blocks have been commented out
#Question 9: Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is 
#stored in spam, and prints Greetings! if anything else is stored in spam
spam = 0
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')

#Question 13: Write a short program that prints the numbers 1 to 10 using a for loop. 
#Then write an equivalent program that prints the numbers 1 to 10 using 
#a while loop
#using a for loop,
for num in range(1,11):
    print(num)
#using a while loop,
numb = 1
while numb <= 10:
    print(numb)
    numb += 1

