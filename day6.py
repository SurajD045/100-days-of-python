#build in datatype : int , float , complex.
a = 17891234567890
a1 = complex(8 ,2)#thats how we define complex variable in python
print("complex number is ", a1)
print(a)

b = "suraj"
print(b)
c = True
d = None
# print(a+b)    #here we are trying to concatenate the two different data types but it will thros error as on int and other is string 
print("type of a is", type(a))
print("type of b is", type(b))
print("type of b is", type(c))
print("type of b is", type(d))


#sequential datatypes are two:
#1:list where you can have values of different datatypes. 
list1 = [ 1, 2.9 ,[9,0],["bananaaa ,apllpppe"]]  #we can have list in list , also list is mutable means list can be changed anytime.
print("type of list1",list1,"is", type(list1) )


#2: tupple is same as the list except one thing that is tupple is fixed , you cant change it .
tupple1 = (1,3.8,(3,69),"happyjhon",("jk","villan"))
print("type of tupple ",tupple1,"is",type(tupple1))

#mapped data type :dict 
#dict: is an unordered collection of data containing a key:value pair.
#The key:value pairs are enclosed withing curly brackets.
dict1 = {"name":"Suraj","age":21,"employed":True}
print("type of dict1",dict1,"is",type(dict1))
