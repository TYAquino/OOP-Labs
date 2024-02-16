#modules
import math
#print(help(math))
print(dir(math))
print(math.__doc__)

import string as s
print(s.ascii_letters)

import random as r
for i in range(4):
    print(r.random())

for i in range(4):
    print(r.randint(1,10))