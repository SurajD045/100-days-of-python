"""
In a python, anything u enclose between and single and double quotation marks is considered 
as string is essentially a sequence or array of textual data. Stings are used when working 
with the unicode characters .
"""
name = "Suraj"
Friend = "Pranav"
print("hello,"+name)

Msg = '\nHi suraj,"i am big fan of yours"'    #here we have written the double in beween the text 
#so we used the single quote for defining the string
print(Msg)

msg = """\nHii i am writiing multiple lines 
as a text string using tripple double qoute 
so i can write n number of lines and can print them."""

print(msg)

#print location wise
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

print("lets use an for loop to print the whole string characterwise")

for character in Msg:  
    print(character)
