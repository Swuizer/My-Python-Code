# When we are using a finally keyword in function/ anywhere, at any cost(even if some rules are broken) finally keyword execute their statement.
def func():
    try:
        l = [1, 5, 6, 7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0

    finally:
        print("I am always executed")
    # print("I am always executed")

x = func()
print(x)