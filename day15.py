import time 

timeStamp1 = time.strftime('%H:%M:%S')
print(timeStamp1)

timeStamp2 = int(time.strftime('%H'))
print(timeStamp2)

timeStamp3 = time.strftime('%M')
print(timeStamp3)

timeStamp4 = time.strftime('%S')
print(timeStamp4)

if(6<timeStamp2<12):
    print("Good Morning sir!!")
elif(12<timeStamp2<18):
    print("Good afternoon sir!!")
elif(18<timeStamp2<20):
    print("Good Evening Sir!!")
else:
    print("Good Night sir!!")



