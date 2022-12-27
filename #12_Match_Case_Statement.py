# x = 4                                         # Match statement same as switch statement
x = int(input("Enter the value of x: "))
match x:
    case 0:
        print("x is Zero")
    case 4:
        print("x % 2 == 0 and case is 4")       # We do not need to break statement in Python 
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 80")
    case _:
        print(x)
