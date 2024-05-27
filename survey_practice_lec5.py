# script written by MD Zuber
# created on 25/01/2024
#This is a code for plotting elevation data for 7 different point
import numpy as np
distance=np.linspace(0,300,7)
distance=np.array(distance,dtype=int)
elevation=[0,5,8,3,0,18,8]
elevation=np.array(elevation)
elevation=elevation+422
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_subplot(121)
ax.plot(distance,elevation)
ax1=fig.add_subplot(122)
ax1.plot(elevation,distance)
plt.show


