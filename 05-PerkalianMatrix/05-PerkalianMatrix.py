import numpy as np

# Biar ga lupa, perkalian matrix kaya gimana cuy
"""
a1 a2  *  b1 b2  =  (a1*b1)+(a2*b3)     (a1*b2)+(a2*b4)
a3 a4     b3 b4     (a3*b1)+(a4*b3)     (a3*b2)+(a4*b4)
"""

a = np.array(([1,2],
              [3,4]))
b = np.ones([2,2])

print("a: ")
print(a)

print("b: ")
print(b)

# PerKALIan matrix
c = np.dot(a,b)

print("a X b adalah")
print(c)

# Cara KEDUA
d = a.dot(b)
print("Cara ke DUA -> a X b adalah")
print(d)


'''
a: 
[[1 2]
 [3 4]]
b:
[[1. 1.]
 [1. 1.]]
a X b adalah
[[3. 3.]
 [7. 7.]]
Cara ke DUA -> a X b adalah
[[3. 3.]
 [7. 7.]]
'''