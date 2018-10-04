from PIL import Image
import math
import numpy as np

im = Image.open('Brain.jpg')

data = np.asarray(im)
data.setflags(write=1)
inpt = int(input("Number of bits to be converted to "))


def value(intensity, bits):
    return math.ceil((intensity+1)/(2**(8-bits)))*(2**(8-bits))


for i, x in enumerate(data):
    for j, y in enumerate(x):
        a = value(y[0], inpt)
        for k, z in enumerate(y):
            data[i, j, k] = a

img = Image.fromarray(data)
img.show()
