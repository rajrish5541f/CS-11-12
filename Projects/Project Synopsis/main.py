import matplotlib.pyplot as plt
import numpy


x=numpy.array([1,3,4])
y=numpy.array([[1],[3],[4]])

print(x,y, sep='\n')
print(x.ndim, y.ndim)
print(x.shape, y.shape)

print('\n'*4)
a=numpy.array([[1,2],[3,4]])
b=numpy.array([[1,2,3],[3,4,6],[1,2,5]])
print(a,b, sep='\n')
print(a.ndim)
print(a.shape)
print(b.ndim)
print(b.shape)