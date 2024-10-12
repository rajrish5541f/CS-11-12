import matplotlib.pyplot as plt
import numpy as np

# # Standard lines of code
# fig, ax = plt.subplots()
# ax.plot(x,y)
# plt.show()

# plt.style.use('_mpl-gallery')

# make data
x = np.linspace(0, 10, 100)
y = 4 + 1 * np.sin(2 * x)
x2 = np.linspace(0, 10, 25)
y2 = 4 + 1 * np.sin(2 * x2)

# plot
fig, ax = plt.subplots()

ax.plot(x2, y2 + 2.5, 'x', markeredgewidth=2)
ax.plot(x, y, linewidth=2.0)
ax.plot(x2, y2 - 2.5, 'o-', linewidth=2)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()




















# import matplotlib.pyplot as plt
# import numpy
#
#
# x=numpy.array([1,3,4])
# y=numpy.array([[1],[3],[4]])
# a=numpy.array([[1,2],[3,4]])
# b=numpy.array([[1,2,3],[3,4,6],[1,2,5]])
#
# print(x.ndim, y.ndim, a.ndim, b.ndim)
#
#
# new=numpy.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
# new1=numpy.reshape(new, shape=(2,2,2,2))
# print(new1, new1.ndim, new1.shape, sep='\n')