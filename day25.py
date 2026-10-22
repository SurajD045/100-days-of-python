#Manupulating tuple
"""tuples are imutable, hence if you want to add,remove or chnange tuple items, thwn first you must convert the 
tuple to list. then perform operations to list and convert back it to tuple.
"""
# countries = ("India","Spain","germany","Italy")
# temp = list(countries)
# temp.append("Oman")
# temp.pop(3)
# temp[2] = "Japan"
# countries = tuple(temp)
# print(countries)
# countries2 = ("usa","canada","england")
# print(countries2)

# #concatenation of two tuples
# countries3 = countries + countries2
# print(countries3)

#count()
"""The count() method of tuple returns the number of times the given element appears in the tuple."""

tuple = (1,2,3,6,90,5,8,5,9,5,9,5)
res  = tuple.count(5)
print(res)