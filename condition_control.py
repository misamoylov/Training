__author__ = 'Mikhail'
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd

df=pd.read_excel("D:/Python_Projects/Training/zones.xlsx", u"conditions")
fig=plt.figure() #Plots in matplotlib reside within a figure object, use plt.figure to create new figure
#Create one or more subplots using add_subplot, because you can't create blank figure
ax = fig.add_subplot(1,1,1)
ax.hist(df[u'Дата'],bins = 14) # Here you can play with number of bins
#Labels and Tit
plt.title('Data')
plt.xlabel('Data')
# plt.ylabel('#Employee')
plt.show()
