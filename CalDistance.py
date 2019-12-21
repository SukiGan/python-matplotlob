# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 16:38:39 2019

@author: Administrator
"""


import numpy as np

Ax = -13.796
Ay = -12.773
Bx = -15.502
By = -19.375
Cx = 0.445
Cy = -16.627
centerx = 0.0
centery = 0.0

resultAB = np.sqrt((Ax-Bx)*(Ax-Bx)+(Ay-By)*(Ay-By))
resultAC = np.sqrt((Ax-Cx)*(Ax-Cx)+(Ay-Cy)*(Ay-Cy))
resultBC = np.sqrt((Bx-Cx)*(Bx-Cx)+(By-Cy)*(By-Cy))

resultAO = np.sqrt(Ax*Ax+Ay*Ay)
resultBO = np.sqrt(Bx*Bx+By*By)
resultCO = np.sqrt(Cx*Cx+Cy*Cy)

print("A----B::")
print(resultAB)

print("A----C::")
print(resultAC)

print("C----B::")
print(resultBC)

print("A----O::")
print(resultAO)

print("B----O::")
print(resultBO)

print("C----O::")
print(resultCO)