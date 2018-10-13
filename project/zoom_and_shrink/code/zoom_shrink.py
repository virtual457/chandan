import matplotlib.pyplot as plt
import numpy as np


def zoom(array,factor):
    x,y = array.shape
    return np.resize(np.stack((np.resize(np.stack((np.resize(array,((x*y,1))),)*factor,axis=1),(x,y*factor)),)*factor,axis=1),(x*factor,y*factor))

def shrink(array,factor):
    x,y = array.shape
    return np.resize(np.resize(array[[range(0, x, factor)], :], (x//2, y))[:, [range(0, y, factor)]],(x//2,y//2))

img = plt.imread('Brain.jpg')

zoomed_img = zoom(img[:,:,0],factor = 4)
shrinked_img = shrink(img[:,:,0],factor = 2)

plt.imsave('Brain_2x.png',arr=zoomed_img,cmap='gray')
plt.imsave('Brain_0.5x.png',arr=shrinked_img,cmap='gray')
