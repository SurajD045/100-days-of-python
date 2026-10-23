#string formatting in python.This is old method
"""string formatting can be done in python using the format method:"""
letter = "hey my name is {1} and I am from {0}"
country = "India"
name = "Suraj"
print(letter.format(country,name))

# f-string in prthon.
""" It is new string formating mechanism introdued by the PEP 498
it is also known as literal string Interpolationor more commonly as f-string(if character preceding the string literal.)
The primary focus of this mechanism is to make the interpolation easier."""

"""When we prefix the string with the letter "f",the string become the f-string itself. The f-string can be formated, in much same as 
the str.format() method.the f-string offers convenient way to embed python expression inside string literal for formatting.
"""
print(f"Hey my name is {name},and i am in {country}")