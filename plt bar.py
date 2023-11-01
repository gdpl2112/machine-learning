import matplotlib.pyplot as plt

# 柱状图

language_name = ["java", "kotlin", "js", "python"]

x = range(len(language_name))

y = [52, 9, 20, 19]

plt.figure()

plt.bar(x, y, color=["y", "c", "m", "y"], width=0.5)

plt.grid(linestyle="--", alpha=0.7)

plt.title("常用对比")

plt.show()
