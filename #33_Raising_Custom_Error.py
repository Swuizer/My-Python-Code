a = input("Enter any value between 5 and 9 ")    
if(a == 'quit'):
    print("Ok")
    exit()
else:
    a = int(a)

if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")

print("Your code executed properly")

# a = int(input("Enter any value between 5 and 9 "))

# if(a<5 or a>9):
#     raise ValueError("Value should be between 5 and 9")
