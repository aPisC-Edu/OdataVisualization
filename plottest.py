import numpy as np
import matplotlib.pyplot as plt
'''
fig = plt.figure()  # an empty figure with no axes
fig.suptitle('No axes on this figure')  # Add a title so we know which it is

fig, ax_lst = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes
plt.show()


'''

x = np.linspace(-1, 1, 1000)
y1 = x**3 + 4 * x**2 - 2*x - 3

fig, ax = plt.subplots()

ax.plot(x, y1, label='linear')
#ax.plot(x, y1**2, label='quadratic')
ax.plot(x, y1**3, label='cubic')

plt.xlabel('x label')
#ax.ylabel('y label')

plt.title("Simple Plot")

ax.legend()

plt.show()