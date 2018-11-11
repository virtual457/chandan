def encrypt(c,f):
	a=[]
	f=f.lower()
	add=int(c)
	index={}
	a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	index={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
	l=len(f)
	res=[]
	for i in f:
		key=0
		while (i!=a[key]):
			key=key+1
		if (i==a[key]):
			key=key+add
		if(key >=26 or key <=0):
			key=key%26		
		res.append(a[key])	
	print("\n\n")
	print("plain text")						
	print("".join(map(str,f)))					
	print("\n\n")
	print("encrypted text")						
	print("".join(map(str,res)))					
	print("\n\n")								
	return res					
