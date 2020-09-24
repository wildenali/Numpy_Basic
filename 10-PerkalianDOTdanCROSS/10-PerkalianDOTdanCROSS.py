import numpy as np

a = np.array([1, 3])
b = np.array([3, 0])

# Perkalian Dot
# coba belajar dari sini dulu https://smatika.blogspot.com/2018/09/perkalian-titik-dot-product.html

# perKALIan DOT
c = np.dot(a, b)
print(c)


# perKALIan CROSS
# Coba pelajari untuk refresg tentang cross https://www.fisikabc.com/2017/06/perkalian-silang-dua-vektor.html

# perKALIan CROSS
d = np.array([1, 2, 0])
e = np.array([2, 1, 0])
f = np.cross(d, e)
g = np.cross(e, d)
print(f)
print(g)
