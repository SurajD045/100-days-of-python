#Dicttionary methods:


"""1.update():this methods update the value of th e 
 key provided to it if the item is already exist in the dictionary. else it create a new key-value pair."""

ep1 = {
    101:30,102:32,103:40,105:60,108:99
}
ep2 = {
    104:50,106:90,107:80
}

# ep1.update(ep2)
# print(ep1)

"""2.clear() removes all the items of the dictionary."""
# ep2.clear()

"""3.pop() method removes the key value pari whose key is passed as parameter.
"""
# print(ep2)
# ep2.pop(106)
# print(ep2)

"""popitem() method removes the last key value pair frm the dictionary.
"""
# print(ep2)
# ep2.popitem()
# print(ep2)
 
"""del:we can also use del keyword to remove dictionary item
"""
# print(ep1)
# del ep1[108]
# print(ep1)
"""if key is not provided then it will delect whole dictionary
"""

