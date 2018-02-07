import sys
import skimage
import numpy
from skimage import io
from skimage import exposure
import os
import random
 
imageFile = os.path.abspath("C:/Users/Mats/Desktop/PythonInn/turtle.pgm")
outFile = os.path.abspath("C:/Users/Mats/Desktop/PythonUt/turtle_out.pgm")

image = skimage.img_as_ubyte(io.imread(imageFile))

histogram = [random.randint(1,255) for _ in range(256)]

# using scikit image
# equalized = exposure.equalize_hist(image)

# manual approach follows

# Find dimensions (this presupposes a grayscale image)
height, width = image.shape

# Create bins for histogram
bins = [0]*256

# Collect histogram by traversing the image row by row
for i in range(height):
  for j in range(width):
    bins[image[i,j]] += 1

# Transform the image by mapping through ss
out = numpy.zeros((height, width), numpy.uint8)
for i in range(height):
  for j in range(width):
    out[i,j] = histogram[image[i,j]]

# Save image
io.imsave(outFile, out)