#set methods:
s1 = {1,3,4,8,5,7}
s2 = {2,4,1,6,8}
"""
Joining sets:sets in prython more or less works in same way as sets in mathematics.we can perform operations
union and intersection on the sets just like in mathematics.

1.UNION AND UPDATE: The union() and update() methods prints all items that are pesent in the two sets.
The union method return a new set whereas update()add items into the existing set from another set.

"""
# s3 = s1.union(s2)
# print(s3)
# print("s1=",s1,"s2=",s2)
# s1.update(s2)
# print("s1=",s1,"s2=",s2)

"""2.intersection() and intersection_update():
intersection() methods print only items that are similar to both sets.
the intersection method return a new set whereas intersection_update()method update into the existing state
from another set.
"""
# s3 = s1.intersection(s2)
# print(s3)
# print("s1=",s1,"s2=",s2)
# s1.intersection_update(s2)
# print("s1=",s1,"s2=",s2)

"""3.Symmetric_differece() and symmetric_difference_update():
Method prints only items that are not similar to both the sets."""
s3 = s1.symmetric_difference(s2)
print("symmetric:",s3)

"""4.differece() and differnce_update():
    Methods prints only items that are only present in the original set and not in both sets. """
s3 = s1.difference(s2)
print("difference:",s3)

"""Set methods:
there are several built in methods used for the manipulation of the set. they are explained below.

1.isdisjoint():this method checks if items of given set are present in another set.
this method return false if items are present, else it reurns true.
"""

print("isdisjoint:",s1.isdisjoint(s2))

"""2.issuperset():this method checks if all the items of particular 
set are present in original set.it returns tru if all items are present else return false."""

print("issuperset:",s1.issuperset(s2))

"""3.issubset():this method checks if all the items of all original set are present in perticular set. 
it returns true if all the items are present, else it returns false."""

"""4.add(): if you want to add a single item to the set use add() method """
s2.add(12)
print(s2)

"""5.remove()/discard():we can use remove()or discard methods to remove items from list."""

s2.remove(2)
print(s2)   

"""6. pop():this method removes the last item of the set but the catch up is that we dont knnow
 which item is gets popped as sets are unordered.however you can access the popped item if you assign the
  pop() method to aa variable. """

print("before pop",s1)
a = s1.pop()
print("poped item:",a,"after poped:",s1)

