#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:07:37 2017

@author: lauracaggiano
"""

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

"""
Load data sheets

"""
x1 = pd.ExcelFile('HistologyDataPythonNorm.xlsx')
"""x2 = pd.ExcelFile('HistologyDataPythonTot.xlxs')"""
df1 = x1.parse('Sheet1')
"""df2 = x2.parse('Sheet2')"""

Week1AvgNP = df1.loc[(df1['Patch']=='N') & (df1['Week'] == 1)]
Week1AvgP = df1.loc[(df1['Patch']=='Y') & (df1['Week'] == 1)]

Week2AvgNP = df1.loc[(df1['Patch']=='N') & (df1['Week'] == 2)]
Week2AvgP = df1.loc[(df1['Patch']=='Y') & (df1['Week'] == 2)]

Week3AvgNP = df1.loc[(df1['Patch']=='N') & (df1['Week'] == 3)]
Week3AvgP = df1.loc[(df1['Patch']=='Y') & (df1['Week'] == 3)]

"""
These are the histograms that I want to make up the violin plots
"""

plt.plot(Week1AvgNP['Angle'], Week1AvgNP['Norm Coll'])
plt.figure()
plt.plot(Week1AvgP['Angle'], Week1AvgP['Norm Coll'])
plt.figure()
plt.plot(Week2AvgNP['Angle'], Week2AvgNP['Norm Coll'])
plt.figure()
plt.plot(Week2AvgP['Angle'], Week2AvgP['Norm Coll'])
plt.figure()
plt.plot(Week3AvgNP['Angle'], Week3AvgNP['Norm Coll'])
plt.figure()
plt.plot(Week3AvgP['Angle'], Week3AvgP['Norm Coll'])

""" 
This is my attempt at a violin plot
You can see it's not plotting the data that I want to show
The x axis should be weeks, the y axis should be angle
The magnitude of the histogram should correspond to Norm Coll
"""

plt.figure()
ax = sns.violinplot(x = "Week", y = "Angle", hue = "Patch", data = df1, palette = "muted", split = True)
