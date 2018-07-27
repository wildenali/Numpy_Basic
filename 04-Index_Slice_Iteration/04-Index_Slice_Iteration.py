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
