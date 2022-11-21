bh=(0,0,0)
Rstar=1 #sunradius
Mstar=1 #sunmasses
Mbh=5*10**6 #sunmasses
rt=Rstar*(Mbh/Mstar)**(1/3)
print(rt)
def infl_bh(point,Rt=rt):
    rs=(point[0]**2+point[1]**2+point[2]**2)**(1/2)
    if Rt>rs:
        return 1
    else: 
        return 0

from __future__ import print_function, division
import numpy as np
from PyAstronomy import pyasl
import matplotlib.pylab as plt

# Instantiate a Keplerian elliptical orbit with
# semi-major axis of 170 length units,
# a period of 2 time units, eccentricity of 0.5,
# longitude of ascending node of 70 degrees, an inclination
# of 10 deg, and a periapsis argument of 110 deg.
ke = pyasl.KeplerEllipse(180, 2., e=0.5, Omega=70., i=10.0, w=110.0)

# Get a time axis
t = np.linspace(0, 1.9, 200)

# Calculate the orbit position at the given points
# in a Cartesian coordinate system.
pos = ke.xyzPos(t)

# Calculate orbit radius as a function of the
radius = ke.radius(t)

# Calculate velocity on orbit
vel = ke.xyzVel(t)

# Find the nodes of the orbit (Observer at -z)
for i in range(200):
    if infl_bh(pos[i])==1:
        plt.plot(pos[i,0],pos[i,1],'go')
    else:
        plt.plot(pos[i,0],pos[i,1],'ro')

# Plot x and y coordinates of the orbit
plt.plot([0], [0], 'k+', markersize=9)
plt.show()




radius = ke.radius(t)
plt.plot(t,radius,label="Radius of star")
r=np.zeros(200)
plt.plot(t,r+rt,label="Tidal Radius")
plt.legend()
plt.show()