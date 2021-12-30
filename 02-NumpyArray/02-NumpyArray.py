import numpy as np

# membuat vektor
a = np.array([1, 2, 3, 4, 5])
b = np.array([1.5, 2.5, 5, 6, 7])

# Cara membuat vektor dengan range
c = np.arange(1, 10, 2)  # 1 sampai 10, dengan kenaikan 2

# Cara membuat LINSPACE, adalah Liniear Space
# rentang dari 1 sampai 10, dengan menampilkan 4 buah angka dengan jarak yg sama antara 4 buah angka tersebut
d = np.linspace(1, 10, 4)

# Cara membuat ARRAY MULTIDIMENSI / MATRIX
# baris pertama (1,2,3), baris kedua (4,5,6)
e = np.array([(1, 2, 3), (4, 5, 6)])

# Cara membuat MATRIX nilai nol
f = np.zeros((5, 5))

# Cara membuat MATRIX nilai SATU
g = np.ones((5, 5))

# Cara membuat MATRIX IDENTITAS adalah cari gugel dulu, sekalian belajar matrix lagi
h = np.identity(5)
i = np.eye(5)  # dengan cara ini juga bisa
# Tamplikan di terminal
print('a', a)
print('b', b)
print('c', c)
print('d', d)
print('e', e)
# testing matrix, karena skalar semuanya di tambah 1 akan mejadi berubah angkanya jadi +1 semuanya
print('e', e + 1)
print('f', f)
print('g', g)
print('h', h)
print('i', i)



'''
a   [1 2 3 4 5]
b   [1.5 2.5 5.  6.  7. ]
c   [1 3 5 7 9]
d   [ 1.  4.  7. 10.]
e  [[1 2 3]
    [4 5 6]]
e  [[2 3 4]
    [5 6 7]]
f  [[0. 0. 0. 0. 0.]
    [0. 0. 0. 0. 0.]
    [0. 0. 0. 0. 0.]
    [0. 0. 0. 0. 0.]
    [0. 0. 0. 0. 0.]]
g  [[1. 1. 1. 1. 1.]
    [1. 1. 1. 1. 1.]
    [1. 1. 1. 1. 1.]
    [1. 1. 1. 1. 1.]
    [1. 1. 1. 1. 1.]]
h  [[1. 0. 0. 0. 0.]
    [0. 1. 0. 0. 0.]
    [0. 0. 1. 0. 0.]
    [0. 0. 0. 1. 0.]
    [0. 0. 0. 0. 1.]]
i  [[1. 0. 0. 0. 0.]
    [0. 1. 0. 0. 0.]
    [0. 0. 1. 0. 0.]
    [0. 0. 0. 1. 0.]
    [0. 0. 0. 0. 1.]]
'''