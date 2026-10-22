#string slicing

names = "suraj,pranav,sangram"
print(len(names))  # return the lenght of string 

print(names[0:5])  ##inclusing 0 but not 5. (n-1)
print(names[6:12])  ##inclusing 6 but not 12. (n-1)
print(names[13:])   ##inclusing 13 but not n. (n-1)

print(names[0:-8])  #equivalent to names[0:len(names)-8]
