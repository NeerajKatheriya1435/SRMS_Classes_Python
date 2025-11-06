import math
result = math.sqrt(9)
print(result)  # Output: 3.0

# from keyword:
from math import sqrt
result = sqrt(9)
print(result)  # Output: 3.0

# importing everything:
from math import *
 
result = sqrt(9)
print(result)  # Output: 3.0
 
print(pi)  # Output: 3.141592653589793

# The "as" keyword:
import math as m

result = m.sqrt(9)
print(result)  # Output: 3.0
 
print(m.pi)  # Output: 3.141592653589793

import math
print(dir(math))

