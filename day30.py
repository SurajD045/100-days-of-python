#recusion in python
"""
>>recursion is the process of defining something in terms of itself.

>>Physical world example would be to place two prallel mirrors facing each other , Any object in between them would be reflected recurssively.

>>In python , we know that the function can call the other functions . It is even possible for the function to call itself.
These type of construct are termed as recursive function.

"""
n = int(input("enter the number :"))
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

Factorial = fact(n)
print("the factorial of ",n,"is",Factorial)


