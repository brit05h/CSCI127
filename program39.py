#name: Britney Huiracocha
#email: britney.huiracocha44@myhunter.cuny.edu
#date: November 2,2020
#this program fills in the missing functions


import numpy as np
import matplotlib.pyplot as plt

def average(region):
     """
     Takes a region of an image and
     Returns the average red, green, and blue values across the region.
     """
     
     red, green, blue = 0,0,0  #<-- placeholder, can remove once defined.

     red=np.average(region[:,:,0])
     green=np.average(region[:,:,1])
     blue=np.average(region[:,:,2])

     return(red,green,blue)

def setRegion(region, r,g,b):
     """
     Takes a region of an image and red, green, and blue values, r, g, b.
     Sets the region so that all points have
     red values of r, green values of g, and blue values of b.
     """

     region[:,:,0]=r
     region[:,:,1]=g
     region[:,:,2]=b

######################################################################
### DO NOT CHANGE ANYTHING BELOW THIS LINE                         ###
######################################################################
