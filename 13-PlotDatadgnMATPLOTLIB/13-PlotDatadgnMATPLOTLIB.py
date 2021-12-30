# Matplotlib itu adalah
# cara membuat plot
import numpy as np
import matplotlib.pyplot as plt

# Persamaan GARIS
# y = 2x + 3

x = np.arange(0,11,1)
y = 2*x + 3
print(x)
print(y)
plt.figure(1)
plt.plot(x,y)



# LINGKARAN
jari2 = 5
sudut = np.linspace(0,2*np.pi,100)
x2 = jari2*np.cos(sudut)
y2 = jari2*np.sin(sudut)
plt.figure(2)
plt.plot(x2,y2)

# Menampilkan semua figure
plt.show()



'''
[ 0  1  2  3  4  5  6  7  8  9 10]
[ 3  5  7  9 11 13 15 17 19 21 23]
'''