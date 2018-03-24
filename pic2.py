#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0, 2 * np.pi, .02)
print(theta)

plt.subplot(121, polar=True)
plt.plot(theta, 2 * np.ones_like(theta), lw=2)
plt.plot(theta, theta / 6, '--y', lw=2)

plt.subplot(122,polar=True)
plt.plot(theta,np.cos(5*theta),'--r',lw=2)
plt.plot(theta,2*np.cos(4*theta), 'b', lw=2)
plt.rgrids(np.arange(0.5,2,0.5),angle=45)
plt.thetagrids([0,45,90])

plt.show()
