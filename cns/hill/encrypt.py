import numpy as np
def encrypt(c):
	f=[]
	f=c
	a=[]
	index={}
	a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	index={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
	l=len(f)
	iseven=l%2
	m=[[19,4],[12,15]]
	if (iseven==0):
		print("the string is even")
	else:
		print("the string is odd")
		f=f + "z"
	print("".join(map(str,f)))
	res=[]
	z=np.array(m)
	m=[]
	for i in f:
		key=0
		while (i!=a[key]):
			key=key+1
			print(key)
		if (i==a[key]):
			m.append(key)
	print(m)
	for i in range(0,len(m)-1,2):
		n=[[m[i]],[m[i+1]]]
		x=np.array(n)
		print(x)
		y=np.matmul(z,x)
		print(y)
		r=y%26
		print(r)
		res.append(a[r[0][0]])
		res.append(a[r[1][0]])
		print(res)
	print("\n\n")
	print("plain text")						
	print("".join(map(str,f)))					
	print("\n\n")
	print("encrypted text")						
	print("".join(map(str,res)))					
	print("\n\n")								
	return res					
encrypt("varuna")