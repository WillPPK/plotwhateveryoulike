#!/usr/bin/python

import pylab
import matplotlib
import numpy as np
import scipy.signal as sc
from matplotlib import rc, rcParams
from matplotlib.pyplot import *
import matplotlib.pyplot as plt

x0 = (np.genfromtxt('PIP2/A9C_1.xvg', usecols=(0))/1000) # change name?
y0 = np.genfromtxt('PIP2/A9C_1.xvg', usecols=(3))*10 # change name?
x1 = (np.genfromtxt('PIP2/A9C_2.xvg', usecols=(0))/1000) # change name?
y1 = np.genfromtxt('PIP2/A9C_2.xvg', usecols=(3))*10 # change name?
x2 = (np.genfromtxt('PIP2/A9C_3.xvg', usecols=(0))/1000) # change name?
y2 = np.genfromtxt('PIP2/A9C_3.xvg', usecols=(3))*10 # change name?
#x3 = (np.genfromtxt('5OYB/A9C_1.xvg', usecols=(0))/1000) # change name?
#y3 = np.genfromtxt('5OYB/A9C_1.xvg', usecols=(3))*-10 # change name?
x4 = (np.genfromtxt('5OYB/A9C_2.xvg', usecols=(0))/1000) # change name?
y4 = np.genfromtxt('5OYB/A9C_2.xvg', usecols=(3))*-10 # change name?
x5 = (np.genfromtxt('5OYB/A9C_3.xvg', usecols=(0))/1000) # change name?
y5 = np.genfromtxt('5OYB/A9C_3.xvg', usecols=(3))*-10 # change name?

#print(len(y1))


y0av = sc.savgol_filter(y0,101,1)
y1av = sc.savgol_filter(y1,101,1)
y2av = sc.savgol_filter(y2,101,1)

#y3av = sc.savgol_filter(y3,101,1)
y4av = sc.savgol_filter(y4,101,1)
y5av = sc.savgol_filter(y5,101,1)


pylab.plot(x0,y0, color='black', alpha = 0.2, linewidth=1, linestyle="-")
pylab.plot(x0, y0av, color='black', alpha = 1, linewidth=1, linestyle="-")

#pylab.plot(x1,y1, color='black', alpha = 0.2, linewidth=1, linestyle="-")
#pylab.plot(x1,y1av, color='black', alpha = 1, linewidth=1, linestyle="-")

pylab.plot(x2,y2, color='black', alpha = 0.2, linewidth=1, linestyle="-")
pylab.plot(x2,y2av, color='black', alpha = 1, linewidth=1, linestyle="-")

#pylab.plot(x3,y3, color='magenta', alpha = 0.2, linewidth=1, linestyle="-")
#pylab.plot(x3,y3av, color='magenta', alpha = 1, linewidth=1, linestyle="-")

pylab.plot(x4,y4, color='magenta', alpha = 0.2, linewidth=1, linestyle="-")
pylab.plot(x4,y4av, color='magenta', alpha = 1, linewidth=1, linestyle="-")

pylab.plot(x5,y5, color='magenta', alpha = 0.2, linewidth=1, linestyle="-")
pylab.plot(x5,y5av, color='magenta', alpha = 1, linewidth=1, linestyle="-")

#pylab.title('PIP2-K67N distance') # change name?
pylab.xlabel( "Time (ns)",  fontsize='12' )
pylab.ylabel( "A9C-position ($\AA$)", fontsize='12' )
pylab.legend(loc=2,prop={"size":12})
v=[0,100,-25,30]
pylab.axis(v)
plt.show()
pylab.savefig("PIP2_Position.png", format='png', dpi=200) # change name?
