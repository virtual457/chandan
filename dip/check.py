import matplotlib.pyplot as plt
arr=plt.imread("moon.jpg")
gamma=input("enter the gamma")
c=arr.shape
print(c)
print(c[0])
print(c[1])
print(c[2])
res=[]
y=c[0]
u=c[1]
i=c[2]
for i in range(0,y):
	temp=[]
	a=0
	for j in range(0,u):
		a=1*arr[i][j][0]**gamma
		res[[i][j][0]]=a
		res[[i][j][1]]=a
		res[[i][j][2]]=a
print("gamma correction over")
print(res)
plt.imsave(res,"result.jpg")	
