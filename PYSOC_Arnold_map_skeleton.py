# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 21:16:31 2024

@author: dhume
"""

import numpy as np

from numba import njit

import matplotlib.pyplot as plt

from PIL import Image

 
@njit # Neat trick


# Write the function body

def ApplyMap(X):
    ''' 
    Returns the matrix, X, having applied the Arnold map once
    '''
    pass


# Find the number of times the map needs to be applied
nMax = 1



img = Image.open("BunnyPic.jpg")

Img = img.resize((100,100)) # Reducing the quality

S0 = Img.getchannel("R") # Taking the red pixels- could be any color, we make it gray after anyway

X = np.array(S0)

 
# Plotting the map until it returns to original
for n in range(0,nMax):

    plt.clf() # Clearing the figure

    plt.imshow(X,cmap = "gray") # 'Reading' the array

    plt.pause(0.01)

    X = ApplyMap(X)
