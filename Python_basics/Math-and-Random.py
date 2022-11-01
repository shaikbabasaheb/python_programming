import math
print(math.ceil(10.2))
print(math.floor(10.2))
a=10
b=-12
print(math.copysign(a,b))
print(a,b)
print(math.fabs(-23))
print(math.factorial(50))
print(math.fsum([12,23,54,56]))
print(math.gcd(10,32))
print(math.pow(2,10))
print(math.sqrt(232))
print(math.sin(60))
print(math.cos(60))
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)

print('Random function')
import random
l=[23,54,23,56,234,456,123,56,23]
print(random.choice(l))
print(random.choices(l,k=2))
print(random.choices(l,k=3))

print(random.choice(range(10,50)))

print(random.choice(range(10,50,3)))

print(random.random())

random.shuffle(l)
print(l)

print(random.uniform(12,34))

'''
==== RESTART: C:/Users/Amazonian/Desktop/ps/Python-basics/Math-and-Random.py ===
11
10
-10.0
10 -12
23.0
30414093201713378043612608166064768844377641568960512000000000000
145.0
2
1024.0
15.231546211727817
-0.3048106211022167
-0.9524129804151563
3.141592653589793
2.718281828459045
6.283185307179586
inf
nan
Random function
234
[234, 54]
[56, 234, 54]
49
22
0.3535239056172399
[456, 123, 56, 234, 23, 23, 23, 54, 56]
15.65486209013724
'''
