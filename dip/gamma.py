import matplotlib.pyplot as plt
import numpy as np
arr=plt.imread("blow.jpg")
gamma=float(input("enter the gamma value"))
res=[]
for i in arr:
	temp=[]
	a=0
	for j in i:
		a=int(1*j[0]**gamma)
		temp.append([a,a,a])
	res.append(temp)
print("gamma correction over")
res1=np.array(res)
plt.imsave("result.png",arr=res1)
