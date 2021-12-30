import numpy as np

# Membuat matrix dengan TIPE DATA tertentu, int, float, bool
a = np.array(([1,2,3],[4,5,6]),dtype = float)


# Membuat matrix dengan menggunakan FUNCTION
def kuadrat(baris, kolom):
    return kolom**2

def jumlah(baris, kolom):
    return (kolom + baris)

# b = np.fromfunction(fungsi, ukuran matrix, tipe)
# print(kuadrat(1,5))
b = np.fromfunction(kuadrat, (1,10), dtype = int)
c = np.fromfunction(jumlah, (4,4), dtype = float)
cc = np.fromfunction(jumlah, (3,5), dtype = float)


# Membuat Array atau Matrix dengan ITERABLE
iterable = (x*x for x in range(5))
d = np.fromiter(iterable, dtype = int)

# MULTIPLE Array
dtipe = [('nama','S255'), ('tinggi',int)]
data  = [   #ini adalah list
        ('ucup', 150),
        ('otong', 160),
        ('mario', 180),
        ]

e = np.array(data, dtype = dtipe)

print('a\n', a)
print('b\n', b)
print('c\n', c)
print('cc\n', cc)
print('d\n', d)
print('data\n', data)
print('e\n', e)



'''
a
 [[1. 2. 3.]
 [4. 5. 6.]]
b
 [[ 0  1  4  9 16 25 36 49 64 81]]
c
 [[0. 1. 2. 3.]
 [1. 2. 3. 4.]
 [2. 3. 4. 5.]
 [3. 4. 5. 6.]]
d
 [ 0  1  4  9 16]
data
 [('ucup', 150), ('otong', 160), ('mario', 180)]
e
 [(b'ucup', 150) (b'otong', 160) (b'mario', 180)]
'''