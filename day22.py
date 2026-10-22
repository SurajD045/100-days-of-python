"""List are ordered collection of items. they store multiple items in single variable.
list items are seperated by commas and enclosed within square brackets[]
list are changable meaning we can alter them after creation."""

prime = [1,3,5,7]
print(prime)
print(prime[0])#list index 0
print(prime[1])
print(prime[2])
print(prime[3])
print(prime[:])  #= prime[0:len(marks)]
marks = ["ayush",10,"samay",13]
print(marks)
print(marks[-3]) #len(marks)-3.

"""Check wether an item is present in the list
this is done using the "in" keyword"""
if 5 in prime:
    print("yes")
else:
    print("no")


"""List Comprehension:  List comprehensions are used for creating new list from other iterables like lists,tuples ,dictionaries
sets,even in arrays and strings.

Syntax : 
list = [expression(item) for item in iterable if condition]

expression : it is the item which being iterated.
Iterable:It can be list , tuples ,dictionaries, sets ,even in arrays and strings.
condition :condition checks if the item should be added to the new list or not.
"""

list = [i*i for i in range(10)]
print(list)
list = [i*i for i in range(10) if i%2 == 0]
print(list)

#enxample:Accept the items with the small letter "o" in new list
names = ["milo","tilo","bill","chalo","ghar","kam"]
nameWith_o = [item for item in names if "o" in item]
print(nameWith_o)