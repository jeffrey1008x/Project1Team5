from pylab import *


def set_up_dependencies():
    import pandas as pd
    from pathlib import Path
    import matplotlib.pyplot as plt
    import numpy as np
    import requests
    from scipy.stats import linregress
    
def box_plot(plt, plot_dict, xlabel, ylabel, output_name):
    fig1, ax1 = plt.subplots()
    ax1.set_ylabel(ylabel)
    ax1.set_xlabel(xlabel)
    plot = ax1.boxplot(
        plot_dict.values(), 
        flierprops = dict(
            markersize= 10, 
            markerfacecolor = "red"
        ),
        showmeans=True
    )
    for line in plot['medians']:
        x, y = line.get_xydata()[1]
        text(x, y, '%.1f' % y, horizontalalignment='right')
    for line in plot['means']:
        x, y = line.get_xydata()[0]
        
        text(x, y, '%.1f' % y, horizontalalignment='right')
    
    ax1.set_xticklabels(plot_dict.keys())
    plt.savefig(output_name)
    plt.show()


def lin_reg(plt, linregress, df, xcol, ycol, xlabel, ylabel):
    x_values = df[xcol]
    y_values = df[ycol]
    (slope, intercept, rvalue, pvalue, stderr) = linregress(x_values, y_values)
    regress_values = x_values * slope + intercept
    line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
    plt.scatter(x_values,y_values)
    plt.plot(x_values,regress_values,"r-")
    x_annotate = df[xcol].min()
    y_annotate = df[ycol].mean()
    #if slope > 0:
    #    y_annotate = df[ycol].max()
    plt.annotate(line_eq,(x_annotate,y_annotate),fontsize=15,color="red")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    print(f"The r-value is: {rvalue}")
    plt.show()