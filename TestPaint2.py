# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:09:03 2019

@author: Administrator
"""
"""
import matplotlib as mpl
import matplotlib.pyplot as  plt

mpl.rcParams["font.sans-serif"]=["SimHi"]
mpl.rcParams["axes.unicode_minus"]=False

#Some simple data
x = [1,2,3,4,5,6,7,8]
y = [3,1,4,5,8,9,7,2]

#create bar
plt.bar(x,y, align="center", color="c", tick_label=["q","a","c","e","r",
                                                    "j","b","p"], hatch="/")

#set x y_axis
plt.xlabel("Box label")
plt.ylabel("Box weight")

plt.show()
"""
"""
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"]=["SimHi"]
mpl.rcParams["axes.unicode_minus"]=False

#Some simple data
x = [1,2,3,4,5,6,7,8]
y = [3,1,4,5,8,9,7,2]

#create bar
plt.barh(x, y, align="center",color="c", tick_label=["q","a","c","e","r",
                                                    "j","b","p"], hatch="/") 

plt.xlabel("Box label")
plt.ylabel("Box weight")

plt.show()
"""
"""
import matplotlib as mpl


import matplotlib.pyplot as plt
import numpy as np

#set score
boxWeight = np.random.randint(0, 10, 100)

x = boxWeight

#plot histogram
bins = range(0,11,1)

plt.hist(x, bins=bins,
         color="g",
         histtype="bar",
         rwidth = 1,
         alpha = 0.6)
#set x, y-axis label

plt.xlabel("Kg")
plt.ylabel("Many")

plt.show()
"""
"""
import matplotlib as mpl
import matplotlib.pyplot as plt

kinds = "A ", "B", "C", "D"

color = ["red","green","Blue","black"]

soldNum = [0.05, 0.45, 0.15, 0.35]

plt.pie(soldNum,
        labels=kinds,
        autopct="%3.1f",
        startangle=60,
        colors = color)


plt.show()
"""

"""
import matplotlib.pyplot as plt
import numpy as np

barSlices = 12

theta= np.linspace(0.0, 2*np.pi, barSlices, endpoint=False)
r =30*np.random.rand(barSlices)

plt.polar(theta, r,
          color = "chartreuse",marker="*",
          mfc = "b", ms=10)

plt.show()

"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

a = np.random.randn(100)
b = np.random.randn(100)

plt.scatter(a,b,
            s=np.power(10*a+20*b,2),
            c=np.random.rand(100),
            cmap=mpl.cm.RdYlBu,
            marker="o"
            )


plt.show()































































