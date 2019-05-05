# python-pendulum-plot
A simple script that propagates the state of a pendulum using python and numpy and plots it using matplotlib

This script uses a second-order forward difference Euler scheme to propagate the state of a pendulum (the angle) 
for large and small angles (no small angle approximation). The data is stored in a numpy array which is then 
plotted using matplotlib. Several different initial velocities are plotted.
