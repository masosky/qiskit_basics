import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

P = np.array([1,1,1]).reshape(-1,1)
v = np.array([1,0,1]).reshape(-1,1)
z = np.linspace(-3,3,100)
X, Y, Z = P + v*z

ax.plot(X, Y, Z)
plt.show()