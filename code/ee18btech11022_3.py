import numpy as np
import matplotlib.pyplot as plt
import time


def dft(x,n):
	
	W = np.zeros((n,n),dtype=np.complex128)
	for i in range(n):
		for j in range(n):
				W[i][j] = np.exp(-2j*np.pi*i*j/n)
	return np.matmul(W,x)

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


dft_time = np.zeros(10)
fft_time = np.zeros(10)

for i in range(10):
	N = 2**i
	x = np.random.randint(1,5,size=N)
	t1 = time.time()
	X_d = dft(x,len(x))
	t2 = time.time()
	X = fft(x,len(x))
	t3 = time.time()
	dft_time[i] = t2-t1
	fft_time[i] = t3-t2
	
axis = 2**np.arange(10)
plt.plot(axis, dft_time, label = 'DFT Computation Time')
plt.plot(axis, fft_time, label = 'FFT Computation Time')
plt.title('DFT vs FFT Computation Times')
plt.xlabel('N')
plt.ylabel('Time of execution (in s)')
plt.xscale('log', basex=2)

plt.legend()

plt.show()
