""""
typecaasting: The conversion of one data type in other data type in python is called type casting or type conversion.

python support wide variety of functions or methods like:int(),float(),str(),ord(),hex(),oct(),tuple(),set(),list(),dict(),etc. 
for the type casting in the python .

Explicit typecasting:the conversion of one data type int another datatype, done via devveloper or programmers 
interventionor manuaaly as per the requirement is known as "explicite type casting"


"""

a = "1"
b = "4"
print(a + b)#gives answer as 14 becouse compiler take a and b as the string not as the nmber .

print( int(a) + int(b)) #this will print the 5 becouse we typecasted the string into integer . 

c = "suraj"
#print(int(c))  #will thro an error becouse , typcasting usually done to valid datatypes . like suraj is already a string.

'''
Implicit type casting:
Data types in python do not have the same level i.e. ordering of data types is not the same in python.
Some of the data types have the same order, and some have lower order.While performing any operations on
variables on different datatypes in python,one of the variables data type will be changed to the higher data type, 
according to the level , one datatype is converted into other by python interpreter itself(automatically).
this is called implicit type casting in python.
'''
#ImplicitTypeCasting:
d = 3.6  #float datatype
e = 8    #interger datatype
print(d + e) #integer is converted to float automatically.
