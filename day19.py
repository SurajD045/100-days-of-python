# x = int(input("enter the number for whivh table yoou want:"))

# for i in range(1,12):
#     if(i>10):
#         """the break statement enables a program to skip over a part of the code . A break statement terminates thevery loop
#         it lies within."""
#         break  #yaha jese hi i >10 hua loop brreak hua. so we use beak when we dont want to implement the conditions.
#     print(x,"x",i,"=",x*i)
# print("break yani loop ko chod kar nikal jao.")

y = int(input("Enter the number for finding its table:"))

for i in range(1,13):
    if(i==10):
        print("skip the iteration")
        continue
    print(y,"x",i,"=",y*i)