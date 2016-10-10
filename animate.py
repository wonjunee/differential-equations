"""
This is the script that animate the data from the python scripts.
The script that is called in execfile function should contain
the data array that contains the series of x values and y values.
"""

import numpy
from matplotlib import pyplot
from matplotlib import animation

# Call the data
# execfile("thermal-programming_data_only.py")
execfile("wind-shift.py")

title = "Heat Conduction"
xlabel = "Position in m"
ylabel = "Temperature in K"

# First set up the figure, the axis, and the plot element we want to animate
fig = pyplot.figure()
ax = pyplot.axes(xlim=(0, 0.2), ylim=(100, 1200))
line, = ax.plot([], [], lw=2)
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

# Labels
axes = pyplot.gca()
pyplot.title(title)
axes.set_xlabel(xlabel)
axes.set_ylabel(ylabel)

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

pyplot.show()