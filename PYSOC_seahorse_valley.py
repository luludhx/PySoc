# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 22:58:33 2022

@author: dhume
"""
import numpy as np
import matplotlib.pyplot as plt

def func(c):
    z = 0
    for i in range(100):
            z = (z ** 2) + c
            if abs(z) > 2:
                return False
    return True

l = []
x_arr = np.linspace(-0.8, -0.78, 1000)
y_arr = np.linspace(0.14, 0.17, 1000)       
for x in x_arr:
    for y in y_arr:
        c = x + y*1j
        if func(c):
                  l.append(c)

re = [i.real for i in l]
im = [i.imag for i in l]
plt, ax = plt.subplots(figsize=(20,20))
ax.set_axis_off()
ax.scatter(re, im, color='indigo', marker='.')
plt.show()

