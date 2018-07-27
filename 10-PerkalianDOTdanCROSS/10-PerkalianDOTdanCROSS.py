import numpy as np

a = np.array([1,3])
b = np.array([3,0])

# perKALIan DOT
c = np.dot(a,b)
print(c)


# perKALIan CROSS
d = np.array([1,2,0])
e = np.array([2,1,0])
f = np.cross(d,e)
g = np.cross(e,d)
print(f)
print(g)
