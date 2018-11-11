import numpy as np
def decrypt(c):
	f=[]
	f=c.lower()
	a=[]
	index={}
	a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	index={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
	l=len(f)
	m=[[5,16],[22,15]]
	res=[]
	z=np.array(m)
	m=[]
	for i in f:
		key=0
		while (i!=a[key]):
			key=key+1
		if (i==a[key]):
			m.append(key)
	for i in range(0,len(m)-1,2):
		n=[[m[i]],[m[i+1]]]
		x=np.array(n)
		y=np.matmul(z,x)
		r=y%26
		res.append(a[r[0][0]])
		res.append(a[r[1][0]])
	print("\n\n")
	print("encrypted text")						
	print("".join(map(str,f)))					
	print("\n\n")
	print("plain text")						
	print("".join(map(str,res)))					
	print("\n\n")								
	return res					
