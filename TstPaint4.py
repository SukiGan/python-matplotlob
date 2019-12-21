# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 21:01:34 2019

@author: Administrator
"""

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(1,6,1)
y = [0,4,3,5,6]
y1 = [1,3,4,2,7]
y2 = [3,4,1,6,5]

labels = ["1","2","3"]

plt.stackplot(x, y, y1, y2, labels=labels)

plt.legend(loc="upper left")

plt.show()