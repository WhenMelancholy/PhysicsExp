#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

w = np.linspace(.1, 1000, 1000)
p = np.abs(1 / (1 + .1j * w))

plt.subplot(221)
plt.plot(w, p, lw=2)
plt.xlabel('X')
plt.ylabel('Y')

plt.subplot(222)
plt.semilogx(w, p, lw=2)
plt.ylim(0, 1.5)
plt.xlabel('log(X)')
plt.ylabel('Y')


plt.subplot(223)
plt.semilogy(w, p, lw=2)
plt.ylim(0, 1.5)
plt.xlabel('X')
plt.ylabel('log(Y)')

plt.subplot(224)
plt.loglog(w, p, lw=2)
plt.ylim(0, 1.5)
plt.xlabel('log(X)')
plt.ylabel('log(Y)')

plt.show()
