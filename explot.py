import numpy as np
import matplotlib.pyplot as plt


def get_err(var, lenght):
    try:
        float(var)
        temp = np.full(lenght, var)
        return temp
    except:
        temp = np.array(var)
        return temp


def get_m_d(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - slope * x1
    return slope, intercept


def main(x, x_err, y, y_err, cfg):

    # Denpendent function
    def abline(slope, intercept, color=cfg['el_color'], linestyle='solid', linewidth=1.75, x=x, y=y):
        '''
        Line form slope and intercept
        '''
        x_vals = np.array([(x[0] + x[-1]) * 0.05, x[0] + x[-1]])
        y_vals = intercept + slope * x_vals
        plt.plot(x_vals, y_vals, color=color,
                 linestyle=linestyle, linewidth=linewidth)

    # Vars
    x = np.array(x)
    y = np.array(y)
    N = len(x)
    x_err = get_err(x_err, N)
    y_err = get_err(y_err, N)

    # Sum
    sum_x = x.sum()
    sum_y = y.sum()
    sum_x2 = (x**2).sum()
    sum_y2 = (y**2).sum()
    sum_xy = (x * y).sum()

    # Linear regression
    m = (N * sum_xy - sum_x * sum_y) / (N * sum_x2 - (sum_x)**2)
    d = (sum_y - m * sum_x) / N

    # Uncertainty line 1 (steeper)
    AB = cfg["range1"]
    x1 = x[AB[0]] - x_err[AB[0]]
    y1 = y[AB[0]] - y_err[AB[0]]
    x2 = x[AB[-1]] + x_err[AB[-1]]
    y2 = y[AB[-1]] + y_err[AB[-1]]
    m1, d1 = get_m_d(x1, y1, x2, y2)

    CD = cfg["range2"]
    x1 = x[CD[0]] - x_err[CD[0]]
    y1 = y[CD[0]] + y_err[CD[0]]
    x2 = x[CD[-1]] + x_err[CD[-1]]
    y2 = y[CD[-1]] - y_err[CD[-1]]
    m2, d2 = get_m_d(x1, y1, x2, y2)

    # Export to stat.txt
    with open('stat.txt', 'w') as rs:
        rs.write(f"""Statistics:
    x = {list(x)}
    x_err = {list(x_err)}
    y = {list(y)}
    y_err = {list(y_err)}
    ∑x = {sum_x}
    ∑x² = {sum_x2}
    ∑y =  {sum_y}
    ∑y² = {sum_y2}
    ∑xy = {sum_xy}
Linear regression line: y = m * x +d
    Slope:      m ={m}
    Intercept:  d = {d}
Uncertainty lines: y = m * x +d
    m_max = m1 = {m1}
    d_min = d1 = {d1}
    m_min = m2 = {m2}
    d_max = d2 = {d2}""")

    # Plot config
    plt.figure(dpi=cfg['dpi'])
    plt.grid(cfg['grid'], linewidth=cfg['grid_width'],
             color=cfg['grid_color'], linestyle='-')
    ax = plt.gca()
    ax.set_facecolor(cfg['ax_background'])
    ax.spines['bottom'].set_color(cfg['ax_axis_color'])
    ax.spines['top'].set_color(cfg['ax_axis_color'])
    ax.spines['right'].set_color(cfg['ax_axis_color'])
    ax.spines['left'].set_color(cfg['ax_axis_color'])
    ax.set_xlim(cfg['x_min'], cfg['x_max'])
    ax.set_ylim(cfg['y_min'], cfg['y_max'])

    # Set titles
    font = cfg['font']
    plt.title(cfg['title'], fontdict=font)
    plt.xlabel(cfg['x_label'], fontdict=font)
    plt.ylabel(cfg['y_label'], fontdict=font)

    # Plot points with error bars
    plt.errorbar(
        x, y, xerr=x_err, yerr=y_err, fmt=cfg['fmt'], ecolor=cfg['ecolor'], elinewidth=cfg['elinewidth'],
        capsize=cfg['capsize'], capthick=cfg['capthick'], ms=cfg['ms'], color=cfg['pcolor']
    )

    # Linear regression line
    abline(m, d, color=cfg['l_color'], linewidth=cfg['l_width'])

    # Uncertainties
    abline(m1, d1, linestyle='dashed')
    abline(m2, d2, linestyle='dashed')

