#functions for importing and exporting images
import PIL.Image as im
import numpy as np
import sys

#import image as a numpy array
#parameters: file name
#returns the 3-dim numpy array representing the image
def imp(file):
    return np.asarray(im.open(file))

#export numpy array as image
#parameters: numpy array representing the image, file name to save
#return: none
def exp(array,file):
    im.fromarray(array).save(file)
