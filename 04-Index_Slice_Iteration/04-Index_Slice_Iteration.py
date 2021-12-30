import numpy as np

a = np.arange(10)**2    # dari 0 dampai 9 di kuadrat kan

print(a)
# Mengambil nilai
print('element ke 1 dari a adalah', a[0])
print('element ke 3 dari a adalah', a[1])
print('element ke 2 dari a adalah', a[2])
print('element ke 4 dari a adalah', a[3])

# SLICE
print('element dari 1-6 dari a adalah', a[0:6]) #[start:end]
print('element dari 4 sampai akhir dari a adalah', a[3:]) #[start:end]
print('element dari AWAL sampai 5 dari a adalah', a[:5]) #[start:end]

# ITERATION
for i in a:
    print('nilai = ', i)


'''
[ 0  1  4  9 16 25 36 49 64 81]
element ke 1 dari a adalah 0
element ke 3 dari a adalah 1
element ke 2 dari a adalah 4
element ke 4 dari a adalah 9
element dari 1-6 dari a adalah [ 0  1  4  9 16 25]
element dari 4 sampai akhir dari a adalah [ 9 16 25 36 49 64 81]
element dari AWAL sampai 5 dari a adalah [ 0  1  4  9 16]
nilai =  0
nilai =  1
nilai =  4
nilai =  9
nilai =  16
nilai =  25
nilai =  36
nilai =  49
nilai =  64
nilai =  81
'''