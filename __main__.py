from netCDF4 import Dataset
import numpy as np
from functools import reduce
import json
import matplotlib.pyplot as plt

# Importing data from NetCDF
fh1 = Dataset('output1.nc')
j = json.loads(fh1.inputfile)

# Get relevant parameters from NetCDF
x = fh1.variables['x'][:]
y = fh1.variables['y'][:]
time = fh1.variables['time'][:]
electrons = fh1.variables['electrons'][:]
mass = fh1.variables['mass'][:]


CMList = []

for l in range(len(time)):
    M = 0
    CM = np.array([0, 0])
    for m in range(len(y)):
        M = M + sum(electrons[l][:][m])
    for i in range(len(x)):
        for n in range(len(y)):
                CM = CM + (1/M) * electrons[l][n][i] * np.array([x[i], y[n]])
    CMList.append(CM)

xlist = []

for element in CMList:
    xlist.append(element[0])

# Plotting CM in x as function of time
plt.plot(time, xlist, 'k.')
plt.xlabel(r't [$\omega_{ci}^2$]', fontsize=14)
plt.ylabel(r'x [$\rho_s$]', fontsize=14)
plt.show()

v = []
for i in range(0, len(xlist)):
    try:
        v.append((xlist[i+1]-xlist[i])/(time[i+1]-time[i]))
    except IndexError:
        break

print(v)
