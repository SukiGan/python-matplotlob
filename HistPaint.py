# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 21:09:52 2019

@author: Administrator
"""

import matplotlib as mpl

mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False

import matplotlib.pyplot as plt
import numpy as np

#Set test score 
scoresT = np.random.randint(0, 100, 10)

x = scoresT

#plot hist
bins = range(0, 101, 10)

plt.hist(x,bins=bins,
         color = "red",
         histtype="bar",
         rwidth=1.0
        )

#set x-y label
plt.xlabel("Test Score")
plt.ylabel("Student Number")

plt.show()
#
#
#
#Example 2 
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False

#Set test Score 
scoreT1 = np.random.randint(0, 100, 100)
scoreT2 = np.random.randint(0, 100, 100)

x = [scoreT1, scoreT2]
colors = ["#00ff00", "#ff0000"]
labels = ["Class A", "Class B"]

bins = range(0, 101, 10)

plt.hist(x,bins=bins,
         color=colors,
         histtype="bar",
         rwidth=1.0,
         stacked=False,
         label=labels)

#Set x y label

plt.xlabel("Student Score")
plt.ylabel("Student Numner")

plt.title("Gxz Hist Test")

plt.legend(loc="upper left")

plt.show()
