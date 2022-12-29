letter = "Hey my name is {0} and I am from {1}"
country = "India"
name = "Arghya"
print(letter.format(name, country))
print(f"Hey my name is {name} and I am from {country}")

price = 49.09999
txt = f"For only {price: .2f} dollars!"
print(txt)
print(type(f"{2*30}"))