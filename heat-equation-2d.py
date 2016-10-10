# QUIZ
# 
# Implement the 2D Heat Equation in the 
# heat_conduction function below.

import numpy
from matplotlib import pyplot
from matplotlib import cm
from matplotlib import animation
import pylab
import time

ambient_temperature = 300. # K
flame_temperature = 1000. # K
thermal_diffusivity = 10. * 0.001 ** 2 # m2 / s
dx = 0.001 # m
size = 50 # grid units
positions = dx * numpy.arange(size) # m
h = 0.01 # s
end_time = 1. # s
num_steps = int(end_time / h)

data = []

def heat_conduction():
    temperatures_old = ambient_temperature * numpy.ones([size, size]) # K
    for iy in range(4 * size / 10, 5 * size / 10):
        for ix in range(4 * size / 10, 5 * size / 10):    
            temperatures_old[iy, ix] = flame_temperature
    temperatures_new = numpy.copy(temperatures_old) # K

    for step in range(num_steps):
        if step % 2 == 0:
            data.append(numpy.copy(temperatures_old))

        for iy in range(1, size - 1):
            for ix in range(1, size - 1):
                ###Your code here.
                temperatures_new[iy, ix] = temperatures_old[iy, ix] + h * thermal_diffusivity / dx ** 2 * \
                            (temperatures_old[iy, ix-1] + temperatures_old[iy, ix+1] \
                            +temperatures_old[iy-1, ix] + temperatures_old[iy+1, ix] \
                            -4 * temperatures_old[iy, ix])
        temperatures_old, temperatures_new = temperatures_new, temperatures_old

    return temperatures_old

temperatures = heat_conduction()

# @show_plot
def plot_me():
    axes = pyplot.gca()
    dimensions = [0, dx * size, 0, dx * size]
    pyplot.imshow(temperatures, cmap = cm.hot,
                             origin = 'lower', extent = dimensions)
    pyplot.colorbar().set_label('Temperature in K')
    axes.set_xlabel('Position x in m')
    axes.set_ylabel('Position y in m')                
    pyplot.show()
plot_me()

# Animation
print "animation start"
# First set up the figure, the axis, and the plot element we want to animate
fig = pyplot.figure()
axes = pyplot.gca()
dimensions = [0, dx * size, 0, dx * size]
im = pyplot.imshow(temperatures, cmap = cm.hot,
                         origin = 'lower', extent = dimensions, animated=True)
pyplot.title('Heat Conduction in 2D: step = 0')
pyplot.colorbar().set_label('Temperature in K')
axes.set_xlabel('Position x in m')
axes.set_ylabel('Position y in m')                


# animation fucntion. This is called sequentially
def animate(i):
    im.set_array(data[i])
    pyplot.title('Heat Conduction in 2D: step = %.1f' % i)
    return im,

# call the animator
print len(data)
anim = animation.FuncAnimation(fig, animate, frames=len(data), interval=10)

pyplot.show()
