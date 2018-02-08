import sys
import skimage
import numpy
from skimage import io
from skimage import exposure
import os
import random
import array
 
imageFile = os.path.abspath("C:/Users/Mats/Desktop/PythonInn/barbara.pgm")
outFile = os.path.abspath("C:/Users/Mats/Desktop/PythonUt/out.pgm")
image = skimage.img_as_ubyte(io.imread(imageFile))

# User Input
values = list()
numValues = int(input("Enter how many elements you want: "))
print('Enter numbers in array: ')
for i in range(int(numValues)):
    n = int(input("Value: "))
    values.append(int(n))

print('Values: ', values)

# Find dimensions (this presupposes a grayscale image)
height, width = image.shape

# Create bins for histogram
bins = [0]*256
bins2 = [0]*256

# Collect histogram by traversing the image row by row
for i in range(height):
  for j in range(width):
    bins[image[i,j]] += 1

# Find cumlated histogram
ss = [0]*256
for k in range(256):
  ss[k] = numpy.uint8(round((255.0/(height*width))*sum(bins[:k]), 0))

# scaling av array for å fylle 256 bøtter
for i in range(256):
    for j in range(numValues):
        bins2[i] = values[j]

ss2 = [0]*256
for k in range(256):
  ss2[k] = numpy.uint8(round((255.0/(height*width))*sum(bins2[:k]), 0))

# inverter array
ssI =[-1]*256
a = 0
for b in range(256):
    ssI[ss2[b]] = b
       
# Transform the image by mapping through ss
out = numpy.zeros((height, width), numpy.uint8)
for i in range(height):
  for j in range(width):
    out[i,j] = ssI[ss[image[i,j]]]

# Save image
io.imsave(outFile, out)