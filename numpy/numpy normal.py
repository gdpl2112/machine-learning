import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.normal(1.75, 1, 100000000)

plt.figure()

plt.hist(x1, 1000)

plt.show()
