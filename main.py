#!/usr/bin/env python

import matplotlib.pyplot as plt
import explot

# INPUTS

x = [2, 4, 6, 8, 10, 12]
y = [42, 48.4, 51.3, 56.3, 58.6, 71]
x_err = 0
y_err = 5

# CONFIGURES

CONFIG = {
    # Label
    'title': '',
    'x_label': 'x',
    'xerr_label': '∆x',
    'y_label': 'y',
    'yerr_lable': '∆y',
    'font': {'family': 'sans-serif',
             'color': '#000000',
             'weight': 'normal',
             'size': 16,
             },

    # Axes
    'ax_axis_color': '#000000',
    'x_min': 0,
    'x_max': (x[0] + x[-1]) * 1.05,
    'y_min': 0,
    'y_max': (y[0] + y[-1]) * 1.05,
    'ax_background': '#ffffff',

    # Graph
    'dpi': 600,
    'grid': True,
    'grid_color': '#d0d0d0',
    'grid_width': 1.5,

    # Error bars
    'ecolor': '#000000',
    'elinewidth': 1.25,
    'capsize': 6,
    'capthick': 1.25,

    # Points
    'fmt': 'o',
    'ms': 5,
    'pcolor': '#16a4a3',

    # Range of error lines (from point A->B)
    'el_color': '#1f77b4',
    'range1': [0, -1],  # Steeper line
    'range2': [0, -1],

    # Linear regression line
    'l_width': 1.5,
    'l_color': '#f8a823'
}

Inverted_Style = False
if Inverted_Style:
    CONFIG['ax_axis_color'] = '#ffffff'
    CONFIG['ax_background'] = '#e6e6e6'
    CONFIG['grid_color'] = '#ffffff'

# Plot
explot.main(x, x_err, y, y_err, CONFIG)
plt.savefig("graph.png")
