#string methods a
#conversion of upper to lower case string and vice versa  

a = "suraj"

print(a)
print(a.upper())

b = "SANGRAM"
print(b.lower())

c = "ohhhhhh !!!!!!!!!! nooohh"
print(c)
print(c.rstrip("!"))

print(c.replace("ohhh","nohh"))
print(c.split(" "))  #converterd the string in list 

#capatilize
"""
the capatilize() methode turns only the first character of string to upper case 
and the rest other characters to lower case.
"""
codeHeading = "welcome to the kurukhetra"
print(codeHeading.capitalize())

"""
center():the center method alignes the string to the center as per the parameters given by the user.
"""
str1 = "Hii my name is suraj."
print(len(str1))
print(len(str1.center(50)))
print(str1.center(50))
"""
we can also add padding character . it will fill the rest of fill characters provided by the users.
"""
print(str1.center(50,"*"))

"""
count(): The count() methode returns the number of times the given values has occured within th given string.
"""
print(str1.count("a"))

#endswith():
#checks if the string ends with the a given value.if yes then return true , else return false.
print(str1.endswith("."))

#we can also checks for a value in-between the string by providing start and end index position
print(str1.endswith("is",1,14))

#find(): The finnd() method searches for the first occurrance of the given value and returns
#the index where it is the present. if the given value is absent from string then return -1.

str2 = "He's man is om ,he is an honest boy"
print(str2.find("is"))

#isalnum(): method return true only if the entire string only consist od A-Z,a-z,0-9.
#if any other character or  punchuations are present , then it returns the false.

str3 = "WelcomeToTheConsole"
print(str3.isalnum())

#isprintable(): this method returns True if all the values within the given string are printable,
#if not return false.

str4 = "we wish you a happy diwal"
print(str4.isprintable())

#isspace(): the isspace() methode returns True only if the string contains white spaces , returns false.
str5 = "   "
print(str5.isspace())