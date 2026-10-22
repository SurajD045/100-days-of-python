"""Function Arguments and return statements:

There are 4 types of arguments that we can provide in function:
    1.Default argument:we can peovide default value while creating a function.This way the fuctionassumes a default
    values even if a value is not provided in the function call for that arguement. 
"""

def name(fname, mname="jhon",lname="whatson"):
    print("hello,",fname,mname,lname)
name("Amy")
"""
    2.keyword argument: we can provide argument with key = value, this way the interpreter recignize the argumentby parameter name
    , hence the order in which the argument posses does not matter.
"""
def name1(fname, mname,lname):
    print("hello,",fname,mname,lname)
name(mname = "jhon",fname = "Amy",lname = "karate")
"""  
    3.variable length argument:In case we dont pass the arguments with a key = value syntax, then it is necessary to pass 
    the arguments in the correct positional order and the number of arguments passed should  match with actual function defination.
"""
def average(a, b ): 
    print("The average is :",(a + b)/2)

average(2, 5)
"""
    4.required argument:Sometimes we may need to pass more arguments than those defined in actual function. 
    this can be done using variable length arguments.:
        There are two ways to achieve this.
        1.Arbitary arguments:
        while creating a function , pass a*  before the parameter name while defining the function. The function access the 
        arguments by processing them in the form of tuple.
        """
def name(*name): #Arbitary arguments:
    print("hello",name[0],name[1],name[2])

name("suraj","hanumant","dubal")

        
def average1(*numbers):
    sum = 0;
    for i in numbers:
        sum = sum + i
    #print("average is :",sum / len(numbers))
    return sum/len(numbers)

A = average1(1,2,3,4,5,6,7,8,9,10)
print("Average is :",A)

""" Keyword arbitary argument:while creating a function  pass a *befor the parameter name while defining the function.
    the function asses the argument by processing them in the form of dictionary.
    """
def name2(**name):
    print("heloo,",name["fname"], name["mname"],name["lname"])

name2(mname = "shiv",lname = "jaganath",fname="raja")