import numpy as np

# Membuat matrix dengan TIPE DATA tertentu, int, float, bool
a = np.array(([1,2,3],[4,5,6]),dtype = float)
print(a)


# Membuat matrix dengan menggunakan FUNCTION
def kuadrat(baris, kolom):
    return kolom**2

def jumlah(baris, kolom):
    return (kolom + baris)

# b = np.fromfunction(fungsi, ukuran matrix, tipe)
# print(kuadrat(1,5))
b = np.fromfunction(kuadrat, (1,10), dtype = int)
c = np.fromfunction(jumlah, (4,4), dtype = float)
print(b)
print(c)


# Membuat Array atau Matrix dengan ITERABLE
iterable = (x*x for x in range(5))
d = np.fromiter(iterable, dtype = int)
print(d)

# MULTIPLE Array
dtipe = [('nama','S255'), ('tinggi',int)]
data  = [   #ini adalah list
        ('ucup', 150),
        ('otong', 160),
        ('mario', 180),
        ]
print(data)

e = np.array(data, dtype = dtipe)
print(e)
