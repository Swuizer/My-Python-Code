dic = {
    "Arghya": "Human being",
    "Spoon": "Object"
}

print(dic)

info = {'name':'Karan', 'age':19,'eligible':True}
print(info)

print(info.get('name2'))
print(info.keys())

for key in info.keys():
    print(info[key])
print(info.values())

print(info.items())

for key, value in info.items():
    print(f"The value corresponding to the key is {value}")