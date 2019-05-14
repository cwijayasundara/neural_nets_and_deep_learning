import numpy as np
import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()
c = np.dot(a,b)

toc = time.time()

print(c)
print("Vectorised version: " + str(1000*(toc-tic)) + " ms")

tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()
print(c)

print("Loop version: " + str(1000*(toc-tic)) + " ms")

