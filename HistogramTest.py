import sys
import skimage
import numpy
from skimage import io
from skimage import exposure
import os

imageFile = os.path.abspath("C:/Users/Mats/Desktop/PythonInn/lena.pgm")
outFile = os.path.abspath("C:/Users/Mats/Desktop/PythonUt/lena_out.pgm")

image = skimage.img_as_ubyte(io.imread(imageFile))

# Find dimensions (this presupposes a grayscale image)
height, width = image.shape

# Define a function for collecting a histogram at (i,j)
def hist(image, i, j):
  bins = [0]*256
  for k in range(max(i-1, 0), min(i+2, height)):
    for l in range(max(j-1, 0), min(j+2, width)):
      bins[image[k,l]] += 1
  return bins

# Transform the image 
out = numpy.zeros((height, width), numpy.uint8)
for i in range(height):
  for j in range(width):
    # Find histogram
    bins = hist(image, i, j)
    # Find the output intensity at (i,j)
    out[i,j] = numpy.uint8(round((255.0/(9))*sum(bins[:image[i,j]]), 0))

# Save transformed image
io.imsave(outFile, out)
