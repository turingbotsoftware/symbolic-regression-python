from math import *
import numpy as np
import matplotlib.pyplot as plt

def prime(x):
    return floor(1.98623*ceil(0.0987775+cosh(log2(x)-0.049869))-(1/x))

data = np.loadtxt('primes.txt')
plt.scatter(data[:,0], data[:,1], label='Data')
plt.plot(data[:,0], [prime(x) for x in data[:,0]], label='Model')
plt.xlabel('N')
plt.title('Prime numbers')
plt.legend()
plt.show()
