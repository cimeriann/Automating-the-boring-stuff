# # # # # # # prices = [10,20,40]
# # # # # # # total = 0
# # # # # # # for item in prices:
# # # # # # #     total += item
# # # # # # # print(f"Total: {total}")
# # # # # # for x in range(4):
# # # # # #     for y in range(3):
# # # # # #         print(f"{x}, {y}")

# # # # # from itertools import count
# # # # # from os import popen, remove


# # # # # numbers = [2, 2, 2, 2, 6]
# # # # # for num in numbers:
# # # # #     if num == 6:
# # # # #         print('xxxxxx')
# # # # #     elif num == 2:
# # # # #         print('xx')
# # # # # # write a program that finds the largest number in a list
# # # # # nums = [3,45,123,346674,11112,42]
# # # # # biggest = nums[0]
# # # # # for i in nums:
# # # # #     if i > biggest:
# # # # #         biggest = i
# # # # # print(biggest)
# # # # #     # .pop: pops a value off the end of a list
# # # # #     # remove
# # # # #     # append
# # # # #     # insert(index,value)
# # # # #     # .count
# # # # #     # .sort
# # # # #     # reverse
# # # # #     # copy
# # # # # print(nums.index(3))
# # # # # # a program that removes duplicates in a list


# # # # from re import I


# # # # nmbs = [1,1,1,2,2,23,3,4,44,4,5,6,7,8,7,4,3,4,5,6,23,43,4,5]
# # # # uniques=[]
# # # # for num in nmbs:
# # # #     if num not in uniques:
# # # #         uniques.append(num)

# # # # uniques.sort()
# # # # print(uniques)

# # # from os import name


# # # matrix = [
# # #     [1, 2, 3],
# # #     [4, 5, 6],
# # #     [7, 8, 9]
# # # ]

# # # for row in matrix:
# # #     for item in row:
# # #         print(item)

# # # coordinates = (1, 2, 3)

# # # x, y, z = coordinates

# # # print(x,y,z)

# # # # dictionaries
# # # Dict = {
# # #     'name': 'john smith',
# # #     'age' : 30,
# # #     'is_verified': True
# # # }
# # # print(Dict['name'])
# # # print(Dict.get('birthdate', 'October 2003'))
# # # print(Dict)
# # # Dict['Weight'] = '70kg'
# # # print(Dict['Weight'])
# # # print(Dict)








# # # phone = input("Phone: ")
# # # digits_mapping = {
# # #     "1" : "One",
# # #     "2" : "Two",
# # #     "3" : "Three",
# # #     "4" : "Four"
# # # }
# # # output = ""
# # # for ch in phone:
# # #     output += digits_mapping.get(ch, "!") + " "

# # # print(output)


# spam = 5
# spam += 10
# print(spam)
# print('four score' \
#     ' and seven years ago')

# bacon = [3.14, 'cat', 11, 'cat', True]
# # bacon.append(99)
# # bacon.remove('cat')
# # del bacon[:2]
# # print(bacon)
# print(tuple([3.14, 'cat', 11, 'cat', True]))

list = [1, 2, 3, 4, 5]
for i in range(0, (len(list))):
    str(list[i]) + ','
list.insert((len(list)-1), 'and')
print(list[len(list)-1])
print(list)