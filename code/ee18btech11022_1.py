import numpy as np
import matplotlib.pyplot as plt


x = np.array([1,2,3,4,2,1])
h = np.zeros(len(x))

h = [ 1, -0.5, 1.25, -0.625, 0.3125,-0.15625]

def dft(x,n):
	
	W = np.zeros((n,n),dtype=np.complex128)
	for i in range(n):
		for j in range(n):
				W[i][j] = np.exp(-2j*np.pi*i*j/n)
	return np.matmul(W,x)


X = dft(x,len(x))
H = dft(h,len(h))
Y = X*H


plt.figure(figsize=(9,15))
plt.subplot(3,2,1)
plt.stem(np.abs(X))
plt.title('$|X(k)|$')
plt.grid()

plt.subplot(3,2,2)
plt.stem(np.angle(X))
plt.title(r'$\angle{X(k)}$')
plt.grid()

plt.subplot(3,2,3)
plt.stem(np.abs(H))
plt.title('$|H(k)|$')
plt.grid()

plt.subplot(3,2,4)
plt.stem(np.angle(H))
plt.title(r'$\angle{H(k)}$')
plt.grid()

plt.subplot(3,2,5)
plt.stem(np.abs(Y))
plt.title('$|Y(k)|$')
plt.grid()

plt.subplot(3,2,6)
plt.stem(np.angle(Y))
plt.title(r'$\angle{Y(k)}$')
plt.grid()

plt.subplots_adjust(hspace=0.4)
plt.show()
