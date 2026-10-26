#python sets :
"""sets are unorderd collection of data items . they store multiple items in a single variable.
set items are seperated by commas and enclosed within curly brakets{}.
sets are unchangeables, meaning you cannot change items of the set once created . 
sets do not create multiple items."""

s = {"chsrly",35,0.9,355,35,"home"}
print(s)

"""
output:{0.9, 'home', 35, 355, 'chsrly'}
here we see that the items of set occurs in random order and hence they cannot be accessed using index 
numbers.Also sets do not allow duplicate values.
"""
harry = set() #defining an empty set.
print(type(harry))
for value in s:
    print(value)
