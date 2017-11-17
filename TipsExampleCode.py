#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 14:00:19 2017

@author: lauracaggiano
"""

"""
Single horizontal violin plot
"""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

plt.figure()
sns.set_style("whitegrid")
tips = sns.load_dataset("tips")
ax = sns.violinplot(x=tips["total_bill"])


"""
Grouped vertically by one catagorical variable
"""
plt.figure()
ax = sns.violinplot(x="day", y="total_bill", data=tips)


"""
Nested grouping
"""
plt.figure()
x = sns.violinplot(x="day", y="total_bill", hue="smoker",data=tips, palette="muted")


"""
Split by hue
* This is what I want to replicate with my data
"""
plt.figure()
ax = sns.violinplot(x="day", y="total_bill", hue="smoker", data=tips, palette="muted", split=True)
