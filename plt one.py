import random

import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

plt.figure()

# plt.plot([1, 2, 3, 4, 5, 6, 7], [29, 28, 39, 30, 19, 17, 19])

plt.grid(True, linestyle="--", alpha=0.7)

x = range(40)

x_ticks_label = ["11点{}分".format(i) for i in x]

y_shanghai = [random.uniform(12, 17) for i in x]
y_beijing = [random.uniform(2, 14) for i in x]

y_ticks = range(40)

plt.plot(x, y_shanghai, label="上海")

plt.plot(x, y_beijing, color="r", linestyle="-.", label="北京")

plt.legend(loc="best")
# plt.legend(loc=0)

plt.xticks(x[::5], x_ticks_label[::5])

plt.yticks(y_ticks[::5])

plt.xlabel("时间")

plt.ylabel("温度/°C")

plt.title("温度表")

plt.savefig("test.jpg")

plt.show()
