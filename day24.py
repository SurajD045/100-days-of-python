#Tupple
"""Tuples are ordered collection of data items. They store multiple items in single variable.
tuple items are seperated by commas and encloosed within round brackets().tuples are unchangeable meaning we cannot alter them after creation."""

tup = (8,5,6,9,63,36,41,14,25,52,"red",True)
print(type(tup), tup)
print(tup[0])
print(tup[5])
print(tup[7])
print(tup[3])
print(tup[1])

#Check for item.
"""we can check if a given item is present in the tuple.this done using the "in" keyword"""
if 41 in tup:
    print("41  is in tuple")
else:
    print("not present")