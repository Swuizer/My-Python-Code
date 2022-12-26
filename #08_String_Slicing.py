# Slicing
name = "Arghya, Rafik"
print(name[2:6])
print(name[0:-3]) # Arghya, Ra    (name[0: len(name) - 3])
print(name[0:len(name) - 3])  # Output: Arghya, Ra

print(name[-1:-3]) # Output:     (null)
print(name[-3:-1]) # Output: fi
print(name[len(name) - 3:len(name) - 1]) # Output: fi

# string length
print(len(name))