#raising Custom errors in python 


"""In python we can raise custom errors by using the raise keyword."""


a = input("Enther the number between 5 and 9:")
if(a=="quit"):
        print("user enterd the quite.")
elif(int(a)<5 or int(a)>9):
        raise ValueError("value should be between 5 and 9")
else:
    print("you enter correct number.")

"""Defining custom exceptions:
In python we can define custom exception by creating a new class
tha is derived from this built in exception class

"""

