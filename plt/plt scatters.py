import random

import matplotlib.pyplot as plt

# 散点图
n = range(100)

x = [random.uniform(0, 300) for i in n]
y = [random.uniform(0, 300) for i in n]

plt.figure(figsize=(20, 8), dpi=100)
plt.scatter(x, y)
plt.show()

