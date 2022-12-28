def calculateGmean(a, b):
    mean = int((a*b)/(a+b))
    print("Total=",mean)
def isGreater(a, b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater")
def isLeaser(a, b):
    pass
a = 9
b = 8

isGreater(a, b)
calculateGmean(a, b)
c = 8
d = 7
isGreater(c, d)
calculateGmean(c, d)