num = int(input("Enter the value of num "))

if(num < 0):
    print("Number is Negative.")
elif(num == 0):
    print("Number is Zero.")
elif(num == 999):
    print("Number is Special.")
else:
    if(num == 2):
        print("Number is Prime")
    else:
        print("Number is positive.")
print("End")
     