import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = [1, 2, 3, 4, 5]

print(a)
print(b)

a = a + 1
# b = b + 1 # ini akan error
b = b + [1]

print(a)
print(b)


'''
[1 2 3 4 5]
[1, 2, 3, 4, 5]
[2 3 4 5 6]
[1, 2, 3, 4, 5, 1]
'''