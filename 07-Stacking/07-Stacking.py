# Stacking itu MENUMPUK

import numpy as np

a = np.array([1,2,3])   # ini ARRAY
b = np.array([4,5,6])   # ini ARRAY

c = np.hstack((a,b))    # Horizontal Stack
d = np.vstack((a,b))    # Horizontal Stack
print(c)
print(d)


aMatrik = np.zeros((2,3))  # ini MATRIX
bMatrik = np.ones((2,3))   # ini MATRIX

cMatrik = np.hstack((aMatrik,bMatrik))
dMatrik = np.vstack((aMatrik,bMatrik))
print(cMatrik)
print(dMatrik)
