# Break
for i in range(12):
    if(i == 10):
        break
    print("5 x",i+1,"=",5 * (i+1))

# Continue 
for i in range(12):
    if(i == 10):
        print("Skip the iteration")
        continue
    print("5 x",i,"=",5 * i)

# create custom do while loop
i = 0
while True:
    print(i)
    i = i + 1
    if(i == 100):
        break 