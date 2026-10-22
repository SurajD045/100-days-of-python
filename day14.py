age = int(input("Enter your age:"))
print("Your age is :",age)

# print(age<18)
# print(age>18)
# print(age<=18)
# print(age>=18)
# print(age==18)

if(age>18):
    print("you can drive")
else:
    print("Your age is below 18 you can't drive")

if(age<0):
    print("You are not born yet!")
elif(age==0):
    print("age is 0")
else:
    print("you are born Child")
    if(age>18):
        print("you can drive")
    else:
        print("Your age is below 18 you can't drive")
