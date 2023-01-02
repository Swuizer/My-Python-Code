a = input("Enter the number: ")                 # Enter any character for checking exception handling
print(f"Multiplication table of {a} is: ")

try:
    for i in range(1, 11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except Exception as e:
    # print(e)
    print("Sorry some Error occurs")

print("Some important lines of code")
print("End of Program")

# Value Error

try:
    num = int(input("Enter an Integer: "))      # Enter any character for checking exception handling
except ValueError:
    print("Number entered is not an integer")

# Index Error

try:
    num = int(input("Enter an Integer: "))      # Enter any number except 0 and 1 for checking exception handling
    a = [6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error")