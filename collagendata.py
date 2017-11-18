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


"""
Loading Data

I created several sheets to see if we can somehow get closer to what you want
to represent, show or plot
"""
x1 = pd.ExcelFile('HistologyDataPythonNorm.xlsx')
df1 = x1.parse('Sheet1')
df2 = x1.parse('Sheet2')                                             # Test sheet... used to show that the graph does not pull a 3rd array
dfw1 = x1.parse('Week1')                                             # As I will try to explain later, this may be the only way of showing your Angle vs. Norm Coll plot
dfw2 = x1.parse('Week2')
dfw3 = x1.parse('Week3')

df1_array = df1.as_matrix(columns=None)                              # Numpy array conversion of the dataframe
dfw1_array = dfw1.as_matrix(columns=None)
dfw2_array = dfw2.as_matrix(columns=None)
dfw3_array = dfw3.as_matrix(columns=None)

"""
Data Extraction

This is the same classification that you built, I am just using a different
tool to plot it
"""

w1np = df1.loc[(df1['Patch']=='N') & (df1['Week'] == 1)]
w1np_array = w1np.as_matrix(columns=None)
w1p = df1.loc[(df1['Patch']=='Y') & (df1['Week'] == 1)]
w1p_array = w1p.as_matrix(columns=None)

w2np = df1.loc[(df1['Patch']=='N') & (df1['Week'] == 2)]
w2np_array = w2np.as_matrix(columns=None)
w2p = df1.loc[(df1['Patch']=='Y') & (df1['Week'] == 2)]
w2p_array = w2p.as_matrix(columns=None)

w3np = df1.loc[(df1['Patch']=='N') & (df1['Week'] == 3)]
w3np_array = w3np.as_matrix(columns=None)
w3p = df1.loc[(df1['Patch']=='Y') & (df1['Week'] == 3)]
w3p_array = w3p.as_matrix(columns=None)

"""
Simple Plot

Same plotting you did, but goruped
"""
# Week 1
plt.figure()
plt.plot(w1np_array[:,0],w1np_array[:,1], "b.")
plt.plot(w1p_array[:,0],w1p_array[:,1], "r.")
plt.xlabel("Angle")
plt.ylabel("Norm Coll")
plt.title("Week 1")
plt.legend({"Y","N"})                                                # Please check that these actually match the with/without patch groups - the array had to be inserted in a weird order
plt.show()

# Week 2
plt.figure()
plt.plot(w2np_array[:,0],w2np_array[:,1], "b.")
plt.plot(w2p_array[:,0],w2p_array[:,1], "r.")
plt.xlabel("Angle")
plt.ylabel("Norm Coll")
plt.title("Week 2")
plt.legend({"Y","N"})                                                # Please check that these actually match the with/without patch groups - the array had to be inserted in a weird order
plt.show()

# Week3
plt.figure()
plt.plot(w3np_array[:,0],w3np_array[:,1], "b.")
plt.plot(w3p_array[:,0],w3p_array[:,1], "r.")
plt.xlabel("Angle")
plt.ylabel("Norm Coll")
plt.title("Week 3")
plt.legend({"Y","N"})                                                # Please check that these actually match the with/without patch groups - the array had to be inserted in a weird order
plt.show()

"""
Histograms

SNS also has some distribution plots that you may want to look at.
These helped me understand what was going on
"""

# Week1 Histogram - Norm Coll (only)
plt.figure()
sns.distplot(w1np_array[:,1])
sns.distplot(w1p_array[:,1])
plt.title("Week 1 - Norm Coll")
plt.xlabel("Norm Coll")

# Week2 Histogram - Norm Coll (only)
plt.figure()
sns.distplot(w2np_array[:,1])
sns.distplot(w2p_array[:,1])
plt.title("Week 2 - Norm Coll")
plt.xlabel("Norm Coll")

# Week3 Histogram - Norm Coll (only)
plt.figure()
sns.distplot(w3np_array[:,1])
sns.distplot(w3p_array[:,1])
plt.title("Week 3 - Norm Coll")
plt.xlabel("Norm Coll")


"""
Boxplot

SNS also has box-plots, which are essentially a segment of the violin plot
"""

# The whole DataSet
plt.figure()
sns.boxplot(x="Week", y="NormColl", hue="Patch", data=df1, palette="PRGn")
sns.despine(offset=10, trim=True)

# WARNING: BE CAREFUL WHEN UNCOMMENTING THIS SECTION
# Note what happens when you try plotting the Angle vs. Norm Coll
# For this plot, I use the data from a single week (otherwise the computer explodes)
# You would also have to change the tickmarks for the x axis

#plt.figure()
#ax = sns.boxplot(x="Angle", y="NormColl", hue="Patch", data=df1, palette="PRGn")
#sns.despine(offset=10, trim=True)

# Trying to plot this made me realize that your collagen normals is already distributed to the angles
# Therefore, I think the only thing you need to do is...

""" 
ViolinPlot

Here is how I think yout violinplot should look like. Technically, your
Collagen Normals dataset has been distributed to the orientation angles.
Look at the similarities between the histogram plots, the boxplot and the
violin plot.

Another hint here was that the violint plot function only takes two dataset,
not three (as you would assume). Essentially, it is expected that the collagen
normal is already a distribution of another controllable variable (in this
case, the angles) - I am like 75% sure hahahah

"""

# This is the plot that you want :)))
plt.figure()
ax = sns.violinplot(x = df1["Week"], y = df1['NormColl'], hue = "Patch", data = df1, palette = "muted", scale="count")
# I do not know how to interpret it, but I am pretty sure you can explain it to me hahaha

plt.figure()
ax = sns.violinplot(x = df1["Week"], y = df1['NormColl'], hue = "Patch", data = df1, palette = "muted", scale="count", inner="quart")

# WARNING: BE CAREFUL WHEN UNCOMMENTING THIS SECTION
#plt.figure()
#ax = sns.violinplot(x = df1["Angle"], y = df1['NormColl'], hue = "Patch", data = df1, palette = "muted", scale="count")
