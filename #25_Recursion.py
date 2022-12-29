# Factorial
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     return n * factorial(n-1)

# res = factorial(7)
# print(res)

# Fibonacci Serice
# f0 = 0
# f1 = 1
# f2 = f1 + f0
# fn = f(n-1) + f(n-2)
list = [0,1,]
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))