# Examples from https://matplotlib.org/users/pyplot_tutorial.html

import matplotlib as mpl
import numpy as np
mpl.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter  # useful for `logit` scale

# Basic
# plt.plot([1,2,3,4], [1,4,9,16])
# plt.axis([0, 6, 0, 20])
# plt.ylabel('some numbers')
# plt.xlabel('some x numbers')
# plt.show()

## Plot using numpy
# t = np.arange(0, 5, 0.2)
# plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
# plt.show()

# Modifying line properties
# t = np.arange(0, 5, 0.2)
# line, = plt.plot(t, t**2)
# # line.set_antialiased(False)
# plt.setp(line, antialiased=False)
# # matlab style
# # plt.setp(line, 'antialiased', False)
# plt.show()

# Working with multiple plots
# plt.figure(1)                # the first figure
# plt.subplot(211)             # the first subplot in the first figure
# plt.plot([1, 2, 3])
# plt.subplot(212)             # the second subplot in the first figure
# plt.plot([4, 5, 6])


# plt.figure(2)                # a second figure
# plt.plot([4, 5, 6])          # creates a subplot(111) by default

# plt.figure(1)                # figure 1 current; subplot(212) still current
# plt.subplot(211)             # make subplot(211) in figure1 current
# plt.title('Easy as 1, 2, 3') # subplot 211 title
# plt.show()


# Creating axes manually
# data
# dt = 0.001
# t = np.arange(0.0, 10.0, dt)
# r = np.exp(-t[:1000]/0.05)
# x = np.random.randn(len(t))
# s = np.convolve(x, r)[:len(x)] * dt # colored noise

# # # the main axes is subplot(111) by default
# plt.plot(t, s)
# plt.axis([0, 1, 1.1*np.amin(s), 2*np.amax(s)])
# plt.xlabel('time (s)')
# plt.ylabel('current (nA)')
# plt.title('Gaussian colored noise')

# # this is an inset axes over the main axes
# a = plt.axes([.65, .6, .2, .2], facecolor='y')
# n, bins, patches = plt.hist(s, 400, normed=1)
# plt.title('Probability')
# plt.xticks([])
# plt.yticks([])

# # this is another inset axes over the main axes
# a = plt.axes([0.2, 0.6, .2, .2], facecolor='y')
# plt.plot(t[:len(r)], r)
# plt.title('Impulse response')
# plt.xlim(0, 0.2)
# plt.xticks([])
# plt.yticks([])

# plt.show()

# TODO :: Need more fundaes on the above. cool Impulse reponse graphs. https://matplotlib.org/examples/pylab_examples/axes_demo.html#pylab-examples-axes-demo

# working with text
# np.random.seed(19680801)
# mu, sigma = 100, 15
# x = mu + sigma * np.random.randn(1000)

# the histogram of the data
# n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

# plt.xlabel('Smarts')
# plt.ylabel('Probability')
# plt.title('Histogram of IQ')
# plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
# plt.grid(True)
# plt.show()

# Annotating text
# ax = plt.subplot(111)

# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2*np.pi*t)
# line, = plt.plot(t, s, lw=2)

# plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#             arrowprops=dict(facecolor='black', shrink=0.05),
#             )

# plt.ylim(-2,2)
# plt.show()

## nonlinear axes
# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure(1)

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()
