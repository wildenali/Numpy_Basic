# Stacking itu MENUMPUK

import numpy as np

a = np.array([1,2,3])   # ini ARRAY
b = np.array([4,5,6])   # ini ARRAY
c = np.hstack((a,b))    # Horizontal Stack
d = np.vstack((a,b))    # Vertical Stack

aMatrik = np.zeros((2,3))  # ini MATRIX
bMatrik = np.ones((2,3))   # ini MATRIX

cMatrik = np.hstack((aMatrik,bMatrik))
dMatrik = np.vstack((aMatrik,bMatrik))

print('a', a)
print('b', b)
print('c', c)
print('d', d)
print('aMatrix\n', aMatrik)
print('bMatrix\n', bMatrik)
print('cMatrix\n', cMatrik)
print('dMatrix\n', dMatrik)
