def set_up_dependencies():
    import pandas as pd
    from pathlib import Path
    import matplotlib.pyplot as plt
    import numpy as np
    import requests
    from scipy.stats import linregress

def box_plot(plt, plot_dict, xlabel, ylabel):
    fig1, ax1 = plt.subplots()
    ax1.set_ylabel(ylabel)
    ax1.set_xlabel(xlabel)
    ax1.boxplot(
        plot_dict.values(), 
        flierprops = dict(
            markersize= 10, 
            markerfacecolor = "red"
        ),
        showmeans=True
    )
    ax1.set_xticklabels(plot_dict.keys())
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