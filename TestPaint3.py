# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 21:03:49 2019

@author: Administrator
"""

"""
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False

#some simple data
x = [1,2,3,4,5]
y = [6,10,4,5,1]

#ceate bar
plt.bar(x,y, align="center",
        color="green  ",tick_label=["A","B","C","D","E"],
        alpha=0.6)

plt.grid(True,axis="y",
         ls=":",color="red",alpha=0.5)

plt.show()
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False

x = np.arange(8)
#benwen
y = [20822910,770889,659687,542629,341184,180033,19167,2]
#By Position marked
y1 = [20864856,766526,618079,551494,352255,203479,26740,24]

bar_width = 0.40
tick_label = ["0-1.5","1.5-3.0","3.0-4.5","4.5-6.0","6.0-7.5","7.0-8.5",
              "8.5-10.0","10.0-11.5"]

#create bar
plt.bar(x,y, bar_width, color="red",
        align="center", label="Method of this article",
        alpha=0.9)

plt.bar(x+bar_width,y1,
        bar_width, color="green",
        align="center",label="Manual Registration",alpha=0.9)

plt.xlabel("Approximate Distances")
plt.ylabel("Point Number")
plt.xticks(x+bar_width/2, tick_label)

plt.title("Approximate distance( values)[8 classes]")
plt.legend()

plt.show()
































