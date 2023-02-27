import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
%matplotlib inline
x = df["Tmin"].to_numpy()
x_100 = x[:100]
x_100
y = df["day"].to_numpy()
y_100 = y[:100]
y_100
plt.plot(x,y, '.')
def line(t, a, b, c):
    return a * np.cos(2*pi*t+b) + c
    from scipy.optimize import curve_fit
from math import pi,cos
popt, pcov=  curve_fit(line, x_100, y_100)
popt
pcov
e=np.repeat(10., 100)
plt.errorbar(x_100,y_100,yerr=e, fmt="none")
popt, pcov=curve_fit(line, x_100,y_100, sigma=e)
popt
print("a= ", popt[0], "+/-", pcov[0,0]**.5)
print("b= ", popt[1], "+/-", pcov[1,1]**.5)
plt.errorbar(x_100,y_100,yerr=e, fmt="none")
xfine=np.linspace(0., 100., 100)
plt.plot(xfine, line(xfine,popt[0], popt[1], popt[2]), 'r-')