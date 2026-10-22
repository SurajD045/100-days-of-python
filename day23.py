#List Methods:
"""1. list.sort():This method sort the list in ascending order . The original list is updated.
"""
# colours = ["red","green","yello","black","white"]
# colours.sort()
# print(colours)

# numbers = [2,6,9,1,16,8,3,22,45,7,5]
# numbers.sort()
# print(numbers)


#2.reverse():
"""this method reverse the order of list"""


# colours = ["red","green","yello","black","white"]
# colours.sort()
# colours.reverse()
# print(colours)

# numbers = [2,6,9,1,16,8,3,22,45,7,5]
# numbers.sort()
# numbers.reverse()
# print(numbers)

#3.index()
"""this method returns the index of the first occurance of the list item ."""

# colours = ["red","green","yello","black","white"]
# #colours.sort()
# print(colours.index("yello"))

# numbers = [2,6,9,1,16,8,3,22,45,7,5]
# #numbers.sort()
# print(numbers.index(16))

#4.count():
"""returns the count of the number of items with the given value ."""

# numbers = [2,6,9,1,16,9,8,3,22,9,45,9,7,5]
# numbers.sort()
# print(numbers)
# print(numbers.count(9))


#5.copy():
"""returns the copy of list.This can be done to perform operations on list without modifying the original list """


# numbers = [2,6,9,1,16,8,3,22,45,7,5]
# numbers.sort()
# print(numbers)

# l = numbers.copy()
# l[0] = 5
# print(l)

#6.insert()
"""this method insert an item at given index. user has to specify the index and item to be inserted within the insert method."""

# colours = ["red","green","yello","black","white"]
# colours.sort()
# print(colours)
# colours.insert(2,"orange")
# print(colours)

# numbers = [2,6,9,1,16,8,3,22,45,7,5]
# numbers.sort()
# print(numbers)
# numbers.insert(6,25)
# print(numbers)

#7.append()
"""This method append the items after the last index of list."""

# numbers = [2,6,9,1,16,8,3,22,45,7,5]
# numbers.sort()
# print(numbers)
# numbers.append(10)
# print(numbers)

#8.extend()
"""This method adds an entire list or any other collection datatype(set,tuple dictionary) to an exiting list."""

l = [2,6,9,1,16,8,3,22,45,7,5]
l.sort()
print(l)

m = [900,1220,23,35,10]
m.sort()
print(m)

# l.extend(m)
# print(l)

#9.concatenate(not a method but a way to concatenate list witout changing l)

k = l + m
print(k)
print(l)
