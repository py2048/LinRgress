import matplotlib.pyplot as plt
import numpy as np

x = np.array([2, 4, 6, 8, 10, 12])
y = np.array([42, 48.4, 51.3, 56.3, 58.6, 71])

slope, intercept = np.polyfit(x, y, 1)


def abline(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals)

plt.scatter(x, y)
abline(slope, intercept)
plt.show()


