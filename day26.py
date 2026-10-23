#exercise:"already practiced in day 15."
"""Should greet according to the time:"""
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

hour = int(time.strftime('%H'))

if(6<hour<12):
    print("Good Morning sir!!")
elif(12<hour<18):
    print("Good afternoon sir!!")
elif(18<hour<20):
    print("Good Evening Sir!!")
else:
    print("Good Night sir!!")
