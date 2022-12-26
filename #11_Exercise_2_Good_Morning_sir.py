import time

print("Welcome to Time World")
myTime = int(time.strftime("%H"))

if(myTime >= 5 and myTime <= 11):
    print("Good Morning Sir")
elif(myTime >= 12 and myTime <= 15):
    print("Good Afternoon Sir")
elif(myTime >= 16 and myTime <= 18):
    print("Good Evening Sir")
elif(myTime >= 19 or myTime <= 4):
    print("Good Night Sir")
else:
    print("False")