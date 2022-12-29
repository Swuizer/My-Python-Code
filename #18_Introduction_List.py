marks = [3,5,6,"Arghya",True]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])

# print(marks[-3]) # Output: 6  (len(marks) - 3)
if 6 in marks:
    print("Available")
else:
    print("Not Available")

# if "Ar" in "Arghya":
#     print("Available")            # Same thing applies for strings as well

print(marks[1:])
print(marks[:5:2]) 

# lst = [i for i in range(4)]
lst = [i for i in range(20) if i%2==0]
print(lst)