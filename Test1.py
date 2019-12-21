# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 15:41:37 2019

@author: Administrator

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.5, 10, 1000)
y = np.cos(x)
y1 = np.random.randn(100)

plt.plot(x,y,ls="--",lw=1,label="plot figure",color="Red") 

plt.legend()

plt.show()



import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.random.rand(1000)


plt.scatter(x,y, label="Scatter Figuer")

plt.legend()

plt.show()
"""
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.random.rand(1000)

plt.scatter(x, y, label="Scatter Figure")

plt.legend()

plt.xlim(0.05, 10)
plt.ylim(0 , 1)

plt.show()
"""
"""
import matplotlib.pyplot as plot
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x,y,ls="-.", lw=2, c="c", label="Plot")

plt.legend()

plt.xlabel("x-axis")
plt.ylabel("y-axis")
"""
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-", lw=2, c="c", label="plot figure")

plt.legend()

plt.grid(linestyle=":", clolor="r")

plt.show()

"""
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)
 
plt.plot(x, y, ls="-.", lw=2, c="c", label="plot figure")

plt.legend()

plt.annotate("maximum",
             xy = (np.pi/2, 1.0),
             xytext=((np.pi/2)+1.0, .4),
             weight = "bold",
             color = "b",
             arrowprops=
             dict(arrowstyle="->", connectionstyle="arc3", color="b")
        )

plt.show()
"""

"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x,y, ls="-",lw=2, color="c",label="plit figure")

plt.legend()

plt.text(3.10, 0.09, "y=sin(x)", weight="bold",  color="blue")

"""
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls="-.", lw=2,c="c", label="figure")

plt.legend(loc="upper left")

plt.title("y=sin(x)")

plt.show()

"""

import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm as cm

#define data
x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)
y1 =np.random.randn(100)

#scatter figure
plt.scatter(x, y1, c="0.25", label="scatter figure")

#plot figure
plt.plot(x, y, ls="--", lw=2, label="plot figure")

#some clean up
#TURN the top spine
for spine in plt.gca().spines.keys():
    if spine == "top" or spine == "right":
        plt.gca().spines[spine].set_color("none")
#turn 
plt.gca().xaxis.set_ticks_position("bottom")

#turn left
plt.gca().yaxis.set_ticks_position("left")

#set x,yaxis limit
plt.xlim(0.0, 4.0)
plt.ylim(-3.0, 3.0)

#set axes label
plt.xlabel("x_labels")
plt.ylabel("y_labels")

# set x,yaxis grid
plt.grid(True, ls=":", color="red")

#add a horizontal line across the axis
plt.axhline(y=0.0, color="r", ls="--", lw=2)

#add a vertical span across the axis
plt.axvspan(xmin=1.0, xmax=2.0, facecolor="yellow", alpha=.3)

#set annotating info 
plt.annotate("maximum",xy=(np.pi/2, 1.0),
             xytext=((np.pi/2+0.15), 1.5),
             weight="bold", color="r",
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="r"))

plt.annotate("spines", xy=(0.75, -3),
             xytext=(0.35, -2.25),
             weight="bold", color="b",
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="b"))

plt.annotate("", xy=(0, -2.78),
             xytext=(0.4, -2.32),
             arrowprops=dict(arrowstyle="->",connectionstyle="arc3", color="blue"))

#set text info
plt.text(3.6, -2.70, "'|' is tickline", weight="bold", color="b")
plt.text(3.6, -2.95, "3.5 is ticklabel", weight="bold", color="b")

#set title
plt.title("strucure of matplotlib")

#set legend
plt.legend()
plt.show()












