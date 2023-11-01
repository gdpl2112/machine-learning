import matplotlib.pyplot as plt
import numpy as np
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.linspace(-10, 10, 100)
y = np.sin(x)

plt.figure(figsize=(20, 8), dpi=100)

plt.plot(x, y)

plt.grid()

plt.show()
