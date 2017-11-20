#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 21:12:07 2017

@author: lauracaggiano
"""
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

x1 = pd.ExcelFile('CollagenAlignmentHistologyMaster.xlsx')
df1 = x1.parse('Sheet1')


#MI410 = df1.loc[(df1['Patch']=='N')]
#MI427 = df1.loc[(df1['Patch']=='Y')]

sns.violinplot(x = "Week", y = "Total Angles",data = df1, hue = "Patch", split = True, bw = .05)