#dictionary in python:

"""Dictionaries are ordered collection of data items. They store multiple 
items in single variable. dictionary items are key value pairs that they are 
seperated by the commas and enclosed within curley bracket{}."""
dic = {
    "harry":"simple human being",
    "spoon":"An non living object"
}

print(dic)

emp = {
    344:"suraj",
    522:"Raj",
    656:"praanav",
    852:"sangram"
}

"""Accessing dictionary items:
values in a dictionary can be accessed using keys. we can
 access dictionary values by mentioning key either in square bracket or by using get method. 
"""
print(emp)
print(emp[344])
print(emp.get(344))

"""Accessing multiple values:
we can print all values in dictionary using values() method.
"""
print("keys ",emp.keys())
print("values",emp.values())

for key in emp.keys():
    print("the keys in dict are",key)
for values in emp.values():
    print("the values of keys are",values)
print("keyss-value pairs:",emp.items())