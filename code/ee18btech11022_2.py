import numpy as np
import matplotlib.pyplot as plt


x = np.array([1,2,3,4,2,1,2,3])


h = np.zeros(len(x))
for i in range(len(x)):
	temp = 0
	if i >= 0:
		temp += pow(-0.5,i)
		if i>= 2:
			temp += pow(-0.5,i-2)
	h[i] = temp

h= [ 1, -0.5, 1.25, -0.625, 0.3125, -0.15625, 0.078125, -0.0390625]
print(h)

def fft(x,n):	

	if(n==1):
		return x
	
	X1 = fft(x[::2],n//2)
	X2 = fft(x[1::2],n//2)
	
	D = np.zeros((n//2,), dtype=np.complex128)
	for i in range(n//2):
		D[i] = np.exp(-2j*np.pi*i/n)
	
	X_u = X1 + D*X2
	X_l = X1 - D*X2
	
	return np.hstack((X_u,X_l))


X = fft(x,len(x))
H = fft(h,len(h))
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
