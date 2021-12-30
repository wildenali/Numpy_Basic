import numpy as np

A = np.array([(2,3),(1,2)])
Y = np.array([23,14])

A_inv = np.linalg.inv(A)

# Menyelesaikan Persamaan LINEAR
X = np.dot(A_inv,Y)


# Cara Lain
X2 = np.linalg.solve(A,Y)

print(A)
print(Y)
print(X)
print(X2)


'''
[[2 3]
 [1 2]]
[23 14]
[4. 5.]
[4. 5.]
'''