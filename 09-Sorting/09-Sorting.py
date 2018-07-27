# Sorting adalah mengurutkan
import numpy as np

# Cara bikin array random, dan di kali kan dengan 10
# floor ini biar di bulatkan aja ke bawah
a = np.floor(np.random.randn(1,6)*10)

print(a)

# Cara Ambil nilai terbesar dari a tersebut
print('nilai terbesar dari a = ', a.max())

# Cara mendapatkan posisi maksimal dari si a
# Kalau misalnya ada lebih dari 2 buah nilai maksimal yg sama, maka yg di ambil adalah posisi paling pertama
print('posisi si nilai terbesar dari a = ', a.argmax())


# Cara Ambil nilai TERKECIL dari a tersebut
print('nilai TERKECIL dari a = ', a.min())

# Cara mendapatkan posisi si nilai TERKECIL dari si a
# Kalau misalnya ada lebih dari 2 buah nilai TERKECIL yg sama, maka yg di ambil adalah posisi paling pertama
print('posisi si nilai TERKECIL dari a = ', a.argmin())


# Cara MENGURUTKAN nya adalah
print('mengurutkan nilai a:' )
print(np.sort(a))
print(np.argsort(a))
print("\n \n")


# ==== DUA DIMENSI ====
print("==== DUA DIMENSI ====")
b = np.floor(np.random.randn(2,2)*10)
print(b)

# Cara Ambil nilai terbesar dari a tersebut
print('nilai terbesar dari b = ', b.max())

# Cara mendapatkan posisi maksimal dari si b
# Kalau misalnya ada lebih dari 2 buah nilai maksimal yg sama, maka yg di ambil adalah posisi paling pertama
print('posisi si nilai terbesar dari b = ', b.argmax())


# Cara Ambil nilai TERKECIL dari b tersebut
print('nilai TERKECIL dari b = ', b.min())

# Cara mendapatkan posisi si nilai TERKECIL dari si b
# Kalau misalnya ada lebih dari 2 buah nilai TERKECIL yg sama, maka yg di ambil adalah posisi paling pertama
print('posisi si nilai TERKECIL dari b = ', b.argmin())


# Cara MENGURUTKAN nya adalah
print('mengurutkan nilai b:' )
print(np.sort(b))
print(np.argsort(b))
print("\n\n")




# CONTOH DATA yg mau di SORTING
print("CONTOH DATA yg mau di SORTING")
dtipe = [('nama','S10'),('tinggi',int)]
data = [
    ('Ucup',170),
    ('Otong',150),
    ('Mario',160)
]

a = np.array(data, dtype = dtipe)
print(a)

# Cara Sorting by tinggi
print(np.sort(a, order='tinggi'))

# Cara Sorting by nama
print(np.sort(a, order='nama'))
