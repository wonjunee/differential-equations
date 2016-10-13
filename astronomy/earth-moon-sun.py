""""
The animation of sun, earth and moon.
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()

ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patch_earth = plt.Circle((5, -5), 0.1, fc='b')
patch_sun = plt.Circle((5, -5), 0.5, fc='r')
patch_moon = plt.Circle((5, -5), 0.05, fc='g')

def init():
    patch_earth.center = (5, 5)
    patch_sun.center = (5, 5)
    patch_sun.center = (5, 5)
    ax.add_patch(patch_earth)
    ax.add_patch(patch_sun)
    ax.add_patch(patch_moon)
    return patch_earth, patch_sun, patch_moon,

def animate(i):
    x, y = patch_earth.center
    x = 5 + 4 * np.sin(np.radians(i))
    y = 5 + 4 * np.cos(np.radians(i))
    patch_earth.center = (x, y)
    patch_moon.center = (x + 0.5 * np.sin(np.radians(i*13.36)), y + 0.5 * np.cos(np.radians(i*13.36)))
    plt.title('Sun Earth Moon: day = %s' % i)
    return patch_earth, patch_moon,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=365, interval=30)

plt.show()