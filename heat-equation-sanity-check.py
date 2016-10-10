# QUIZ
# 
# Find the maximum step size h (to three decimal places) 
# so that the resulting temperatures do not become negative.

import numpy
import matplotlib
import matplotlib.pyplot

ambient_temperature = 300. # K
flame_temperature = 1000. # K
thermal_diffusivity = 10. * 0.001 ** 2 # m2 / s
dx = 0.001 # m
size = 100 # grid units
positions = dx * numpy.arange(size) # m

### Modify h so it does not give nonsensical answers, e.g. temperatures below the ambient temperature.
### Give three decimal places.
h = 0.01 # s
###

end_time = 10.0 # s
num_steps = int(end_time / h)

def heat_conduction():
    temperatures_old = ambient_temperature * numpy.ones(size) # K
    for i in range(4 * size / 10, 5 * size / 10):
        temperatures_old[i] = flame_temperature
    temperatures_new = numpy.copy(temperatures_old) # K

    for step in range(num_steps):
        for i in range(1, size - 1):
            temp = temperatures_old[i]
            temperatures_new[i] = temp + h * thermal_diffusivity / dx ** 2 * (
                temperatures_old[i - 1] + temperatures_old[i + 1] - 2.0 * temp)
        
        temperatures_old, temperatures_new = temperatures_new, temperatures_old

    return temperatures_old

temperatures = heat_conduction()

def plot_me():
    matplotlib.pyplot.plot(positions, temperatures)
    
    axes = matplotlib.pyplot.gca()                
    axes.set_xlabel('Position in m')
    axes.set_ylabel('Temperature in K')
    matplotlib.pyplot.show()

plot_me()

