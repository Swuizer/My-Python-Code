# import math

# from math import sqrt, pi, floor

# This syntax use when we have a require only one or two or some more function.

# from math import *

import math as math_builtin_python

# This syntax use when we have require all function of math.py

floor_to = math_builtin_python.floor(4.2343)
print(floor_to)
result = math_builtin_python.sqrt(9)
print(result)

# from math import pi, sqrt as s

result = math_builtin_python.sqrt(9) * math_builtin_python.pi
print(result)

# print(dir(math_builtin_python))
print(math_builtin_python.nan, type(math_builtin_python.nan))
