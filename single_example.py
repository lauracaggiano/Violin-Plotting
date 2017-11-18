# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 00:05:37 2017

@author: fluviolobo
"""

import seaborn as sns
sns.set_style("whitegrid")
tips = sns.load_dataset("tips")
#ax = sns.violinplot(x=tips["total_bill"])
ax = sns.violinplot(x="day", y="total_bill", data=tips)