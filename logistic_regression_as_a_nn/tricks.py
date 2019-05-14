import numpy as np

a = np.random.randn(5)

print(a)
print(a.shape)
print(a.T)
print(np.dot(a,a.T))

b = np.random.randn(5,1)

print(b)
print(b.shape)
print(b.T)
print(np.dot(b,b.T))

a = np.random.randn(3, 3)
b = np.random.randn(3, 1)
c = a*b
print(c.shape)