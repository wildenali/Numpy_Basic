import numpy as np

# Belajar Invers dan Determinan dulu disini
# https://idschool.net/sma/cara-menentukan-invers-determinan-matriks-dan-sifat-sifatnya/
a = np.array([(1, -1), (1, 1)])

# Inverse Matrix
a_inv = np.linalg.inv(a)    # linalg -> liniear algebra

# DETERMINAN Matrix
det_a = np.linalg.det(a)
det_a_inv = np.linalg.det(a_inv)

# FUNGISNYA si INVERS dan DETERMINAN SALAH sATUNYA adalah
# untuk
# Menyelesaikan PERSAMAAN LINEAR

print(a)
print(a_inv)
print(np.dot(a, a_inv))
print(det_a)
print(det_a_inv)


'''
[[ 1 -1]
 [ 1  1]]
[[ 0.5  0.5]
 [-0.5  0.5]]
[[1. 0.]
 [0. 1.]]
2.0
0.5
'''