import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
arr=plt.imread("chan.jpg")
res=[]
a=[[0,-1,0],[0,2,0],[0,-1,0]]
b=[[0,0,0],[-1,2,-1],[0,0,0]]
ndimage.convolve(arr,a)
ndimage.convolve(arr,b)
n=(input("enter the thresolding value"))
for i in arr:
	temp=[]
	for j in i:
		if(j[0]>n):
			c=255
		elif(j[0]<n+1):
			c=0
		temp.append([c,c,c])
	res.append(temp)
res1=np.array(res)
plt.imsave("result.png",res1)
