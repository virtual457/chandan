import matplotlib.pyplot as plt
import numpy as np
arr=plt.imread("moon.jpg")
size=arr.shape
c=[]
res=[]
b=[]
a=np.array(range(256))
a.fill(0)
for i in arr:
	print(a.shape)
	for j in i:
		u=int(j[0])
		m=a[u]
		n=m+1
		a[u]=n
for i in a:
	b.append(i/(size[0]*size[1]))		
c.append(b[0])
for i in range(1,256):
	c.append((b[i]+c[i-1]))

p=0
o=[]
for i in c:
	o.append(int(i*255))
print(o)
for i in arr:
	temp=[]
	for j in i: 		
		d=o[j[0]]	
		temp.append([d,d,d])
	res.append(temp)
print("gamma correction over")
res1=np.array(res)
plt.imsave("result.png",arr=res1)
