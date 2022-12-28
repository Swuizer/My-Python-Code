# def average(a=9, b=1):      # Default Argument
#     print("The average is",(a + b) / 2)

# average()

def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    # print("Average is:",sum / len(numbers))
    # return sum / len(numbers)

result = average(5,6,8,1)
print(result)