"""
Created on Thu Nov 16 17:07:37 2017

@author: lauracaggiano
@author: fluviolobo
"""

# Import libraries and modules
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Loading data
x1 = pd.ExcelFile('HistologyDataPythonNorm.xlsx')
df1 = x1.parse('Sheet1')

Week1AvgNP = df1.loc[(df1['Patch']=='N') & (df1['Week'] == 1)]
Week1AvgP = df1.loc[(df1['Patch']=='Y') & (df1['Week'] == 1)]

Week2AvgNP = df1.loc[(df1['Patch']=='N') & (df1['Week'] == 2)]
Week2AvgP = df1.loc[(df1['Patch']=='Y') & (df1['Week'] == 2)]

Week3AvgNP = df1.loc[(df1['Patch']=='N') & (df1['Week'] == 3)]
Week3AvgP = df1.loc[(df1['Patch']=='Y') & (df1['Week'] == 3)]

"""
Histograms

- SNS also has some distribution plots that you may want to look at.
  These helped me understand what was going on
"""



#plt.plot(Week1AvgNP['Angle'], Week1AvgNP['Norm Coll'])
#plt.figure()
#plt.plot(Week1AvgP['Angle'], Week1AvgP['Norm Coll'])
#plt.figure()
#plt.plot(Week2AvgNP['Angle'], Week2AvgNP['Norm Coll'])
#plt.figure()
#plt.plot(Week2AvgP['Angle'], Week2AvgP['Norm Coll'])
#plt.figure()
#plt.plot(Week3AvgNP['Angle'], Week3AvgNP['Norm Coll'])
#plt.figure()
#plt.plot(Week3AvgP['Angle'], Week3AvgP['Norm Coll'])


"""
Boxplot
"""

# Draw a nested boxplot to show bills by day and sex
plt.figure()
sns.boxplot(x="Week", y="NormColl", hue="Patch", data=df1, palette="PRGn")
sns.despine(offset=10, trim=True)


""" 
This is my attempt at a violin plot
You can see it's not plotting the data that I want to show
The x axis should be weeks, the y axis should be angle
The magnitude of the histogram should correspond to Norm Coll
"""

plt.figure()
ax = sns.violinplot(x = df1["Week"], y = df1['NormColl'], hue = "Patch", data = df1, palette = "muted", scale="count")
plt.figure()
ax = sns.violinplot(x = df1["Angle"], y = df1['NormColl'], hue = "Patch", data = df1, palette = "muted", scale="count")