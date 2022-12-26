# In Python, anything that you enclose between single and double quotation marks is considered a string.
# A string is essentially a sequence or array of textual data.
# Strings are used when working with unicode character.

name = "Arghya"
friend = "Rohan"
anotherFriend = 'Lovish'
print("Hello",name)

# Multi Line String
print('''He Said,
Hi Arghya
hey I am good''' )

# String is a Sequence of Character
# In most of the programming language indexing start with 0
# 0 1 2 3 4 5
# A r g h y a
print(name[0])
print(name[1])

print("Lets use a for loop\n")
for character in name:
    print(character)