import random

import matplotlib.pyplot as plt
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# 多图
x = range(40)

x_ticks_label = ["11点{}分".format(i) for i in x]

y_shanghai = [random.uniform(12, 17) for i in x]
y_beijing = [random.uniform(2, 14) for i in x]

y_ticks = range(40)

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 8), dpi=100)

axes[0].plot(x, y_shanghai, label="上海")

axes[1].plot(x, y_beijing, color="r", linestyle="-.", label="北京")

axes[0].set_xticks(x[::5])
axes[0].set_yticks(y_ticks[::5])
axes[0].set_xticklabels(x_ticks_label[::5])

axes[1].set_xticks(x[::5])
axes[1].set_yticks(y_ticks[::5])
axes[1].set_xticklabels(x_ticks_label[::5])

axes[0].grid(True, linestyle="--", alpha=0.7)
axes[1].grid(True, linestyle="-", alpha=0.7)


axes[0].set_xlabel("时间")
axes[0].set_ylabel("温度/°C")
axes[0].set_title("上海温度表")

axes[1].set_xlabel("时间")
axes[1].set_ylabel("温度/°C")
axes[1].set_title("北京温度表")

axes[0].legend(loc="best")
axes[1].legend(loc="best")

plt.show()
