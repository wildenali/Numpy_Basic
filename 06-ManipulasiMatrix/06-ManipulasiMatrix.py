# Manipulasi matrix adalah jadi si matrix kita ubah berubah
# misalnya awalnya 2x3, menjadi 3x2 (mengubah bentuknya yakan), dll
# cekidot di bawah aja
import numpy as np

a = np.array((
    [1, 2, 3],
    [4, 5, 6]
))

print('matrix a dengan ukuran:', a.shape)
print(a)


# TRASPOSE -> mengubah bentuknya, misalnya dari 2x3 menjadi 3x2, contohnya seperti dibawah ini
print('traspose matrix dari a:')
print(a.transpose())    # Cara PERTAMA
print(np.transpose(a))  # Cara KEDUA
print(a.T)              # Cara KETIGA


# FLATTEN -> MENSEJAJARKAN, menjadi vector baris
print('flatten matrix a:')
print(a.ravel())    # Hasilnya menjadi [1 2 3 4 5 6]
print(np.ravel(a))  # Hasilnya menjadi [1 2 3 4 5 6]


# RESHAPE -> Mengubah bentuk si matrixnya
print('reShape matrix a:')
print(a.reshape(3, 2))
print(a.reshape(6, 1))


# RESIZE -> Mengubah ukuran si matrixnya
print('reSize matrix a:')
a.resize(3, 2)   # ini adalah cara Mengubah SIZE si matrix a
print(a)
print('matrix a berubah ukuran menjadi:', a.shape)
# liat a.shape di baris 11, dengan a.shape di baris 38, bentuknya menjadi berubah
# karena fungsi RESIZE adalah mengubah ukurannya okeeey



'''
matrix a dengan ukuran: (2, 3)
[[1 2 3]
 [4 5 6]]
traspose matrix dari a:
[[1 4]
 [2 5]
 [3 6]]
[[1 4]
 [2 5]
 [3 6]]
[[1 4]
 [2 5]
 [3 6]]
flatten matrix a:
[1 2 3 4 5 6]
[1 2 3 4 5 6]
reShape matrix a:
[[1 2]
 [3 4]
 [5 6]]
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]
reSize matrix a:
[[1 2]
 [3 4]
 [5 6]]
matrix a berubah ukuran menjadi: (3, 2)
'''