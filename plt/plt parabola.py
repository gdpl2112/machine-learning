import matplotlib.pyplot as plt
import numpy as np

# 抛物线图

x = np.linspace(-10, 10, 100)
y = np.sin(x)

plt.figure(figsize=(20, 8), dpi=100)

plt.plot(x, y)

plt.grid()

plt.show()
