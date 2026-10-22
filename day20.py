#Python functions:

"""Function is a block of code that performs a specific task whenever it is called .
in bigger program, where we have large amounts of code , it is advisable to create or 
use exiting functions that makes the program flow organised and neat. """

"""There are two types of functions:
1.Build in functions
2.user-defined functions.

Built-in functions:
These functions are defined and precoded in python. Som examples of built-in functions are as follows:
main(),max(),len(),sum(),type(),range(),dict(),list(),tuple(),set(),print()etc.

User-defined functions:
We can create functions to performs specific task as per our needs. such functions are called user defined functions."""

# a = 9
# b = 10
# gmean = (a*b)/(a+b)
# print(gmean)

# c = 91
# d = 12
# gmean1 = (c*d)/(c+d)
# print(gmean1)

a = int(input("Enter first number for gmean:"))
b = int(input("Enter second number for gmean:"))
def compare(a,b):
    if(a>b):
        print("the first number is grater")
    elif(a==b):
        print("both numbers are equal")
    else:
        print("second number is greater")
def calculateGmean(a,b):
    gmean = (a*b)/(a+b)
    print("gmean of two numbers ",a,"and",b,"is",gmean)

calculateGmean(a,b)
compare(a,b)