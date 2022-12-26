# Strings are immutable
# a = "!!!Arghya!!!!!!!!"
a = "!!!Arghya !!!! !!!!Arghya"
print(len(a))
print(a.upper()) # a.upper() function return a new string in fully Upper Case.
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Arghya","John"))
print(a.split(" "))
blogHeading = "introduction TO JS"
print(blogHeading.capitalize())
str1 = "Welcome to the console!!!"
print(str1.center(50))
print(len(str1))
print(len(str1.center(50)))
print(a.count("Arghya"))
print(str1.endswith("!!!"))
print(str1.endswith("to",4,10))
print(str1.find("to"))
# print(str1.find("no"))   # Return -1
# print(str1.index("to")) # When you are fully sure, your finding value are available in the string
# print(str1.index("no"))  # Generate a Error
str1 = "WelcomeToTheConsole"
print(str1.isalnum())
print(str1.islower())
print(str1.isprintable())
str1 = "        "
print(str1.isspace())
str1 = "Welcome To The Console"
print(str1.istitle())
str1 = "Python learning"
print(str1.startswith("python"))
print(str1.swapcase())
print(str1.title())