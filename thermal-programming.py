# QUIZ
# 
# Add the model for heat_conduction along 
# a wire to the function heat_conduction 
# below.

import numpy
from matplotlib import pyplot
from matplotlib import animation

ambient_temperature = 300. # K
flame_temperature = 1000. # K
coefficient = 10. # 1 / s
dx = 0.001 # m
size = 100 # grid units
positions = dx * numpy.arange(size) # m
h = 0.01 # s
end_time = 10.0 # s
num_steps = int(end_time / h)

# This is used to keep track of the data that we want to plot.
data = []

def heat_conduction():
    temperatures_old = ambient_temperature * numpy.ones(size) # K
    for i in range(4 * size / 10, 5 * size / 10):
        temperatures_old[i] = flame_temperature
    temperatures_new = numpy.copy(temperatures_old) # K

    for step in range(num_steps):
        if step % 5 == 0:
            data.append(([pos for pos in positions], 
                          [temp for temp in temperatures_old]))
        for i in range(1, size - 1):
            ###Your code here.
            temperatures_new[i] = temperatures_old[i] + h * coefficient * \
                                (temperatures_old[i-1] + temperatures_old[i+1] - 2 * temperatures_old[i])
        # Switch values of temperatures_new and temperatures_old 
        # for the next iteration of the for loop.
        temperatures_new, temperatures_old = temperatures_old, temperatures_new

    return temperatures_old

temperatures = heat_conduction()

# Stationary plot
def plot_me():
    for (pos, temp) in data:
        pyplot.plot(pos, temp)
    axes = pyplot.gca()                
    axes.set_xlabel('Position in m')
    axes.set_ylabel('Temperature in K')
    pyplot.show()

# plot_me()

# Animation

# First set up the figure, the axis, and the plot element we want to animate
fig = pyplot.figure()
ax = pyplot.axes(xlim=(0, 0.1), ylim=(100, 1000))
line, = ax.plot([], [], lw=2)
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)
axes = pyplot.gca()
pyplot.title('Heat Conduction')
axes.set_xlabel('Position in m')
axes.set_ylabel('Temperature in K')

# initialization function: Plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation fucntion. This is called sequentially
def animate(i):
    x = data[i][0]
    y = data[i][1]

    line.set_data(x,y)
    time_text.set_text('step = %.1f' % i)
    return line,

# call the animator
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=len(data), interval=20)

# pyplot.show()

