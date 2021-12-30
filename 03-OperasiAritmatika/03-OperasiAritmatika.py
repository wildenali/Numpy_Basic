import numpy as np

# list python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# array numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

# ===== ELEMENTWISE OPERATION =====
# Penjumlahan
hasilpenjumlahanlist = a + b
hasilJUMLAHarraynumpy = anp + bnp

# Pengurangan
hasilKURANGarraynumpy = anp - bnp

# PerKALIan
hasilKALIarraynumpy = anp * bnp

# PerBAGIan
hasilBAGIarraynumpy = anp / bnp

# KUADRAT
hasilKUADRATarraynumpy = anp**2

# MULTIDIMENSI array Numpy
c = np.array(([1,2,3],[4,5,6]))
d = np.array(([7,8,9],[-1,-2,-3]))
hasilJUMLAHMULTIDIMENSI = c + d
hasilKALIMULTIDIMENSI = c * d

# ===== ELEMENTWISE OPERATION =====


# Menampilkan di Terminal
print(hasilpenjumlahanlist)
print(hasilJUMLAHarraynumpy)
print(hasilKURANGarraynumpy)
print(hasilKALIarraynumpy)
print(hasilBAGIarraynumpy)
print(hasilKUADRATarraynumpy)
print(hasilJUMLAHMULTIDIMENSI)
print(hasilKALIMULTIDIMENSI)    # inget ini perkalian perelement, bukan perkalian matrix seperti matematika yg di pelajari okey, perkalian matrix kaya di pelajaran, di materi selanjutnya


'''
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[ 7  9 11 13 15]
[-5 -5 -5 -5 -5]
[ 6 14 24 36 50]
[0.16666667 0.28571429 0.375      0.44444444 0.5       ]
[ 1  4  9 16 25]
[[ 8 10 12]
 [ 3  3  3]]
[[  7  16  27]
 [ -4 -10 -18]]
'''