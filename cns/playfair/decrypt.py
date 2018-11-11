def decrypt(c,f):
	a=[]

	index={}
	a=["a","b","c","d","e","f","g","h","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	index={"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
	l=len(c)
	print("".join(map(str,a)))
	print("".join(map(str,c)))
	Matrix = [[0 for x in range(5)] for y in range (5)]
	x=0
	y=0
	for i in range (l):
		if (index[c[i]]!=1):
			Matrix[x][y]=c[i]
			y+=1
			if(y==5):
				x+=1
				y=0
			index[c[i]]=1
	print (Matrix)
	for i in range(25):
		if (index[a[i]]!=1):
			Matrix[x][y]=a[i]
			y+=1
			if(y==5):
				x+=1
				y=0
			index[a[i]]=1
	print (Matrix)
	g=len(f)
	res=[]
	p=0
	for i in range(0,g,2):
		flag=1
		print(f[i])
		print(f[i+1])
		for j in range(5):
			for k in range(5):
				if(f[i]==Matrix[j][k]):
					r=j
					s=k
					for e in range(5):
						for d in range(5):
							if(f[i+1]==Matrix[e][d]):
								t=e
								u=d
								if (r==t and s==u):
									res.append(Matrix[r][s])
									res.append(Matrix[t][u])
									flag=0
									break
	
								elif (r!=t and s==u):
									r=r-1
									if(r==-1):
										r=4
									res.append(Matrix[r][s])
									t=t-1
									if(t==-1):
										t=4
									res.append(Matrix[t][u])
									flag=0
									break
					
								elif (r==t and s!=u):
									s-=1
									if(s==-1):
										s=4
									res.append(Matrix[r][s])
									u-=1
									if(u==-1):
										u=4
									res.append(Matrix[t][u])
									flag=0
									break
								
								elif (r!=t and s!=u):
									print("entered into the not equal loop")
									res.append(Matrix[r][u])
									
									res.append(Matrix[t][s])
									flag=0
									print(res)
									break
			
			
	print("given key is:")				
	print("".join(map(str,c)))
	print("\n\n")					
	print("constructed matrix is")					
	print(Matrix)
	print("\n\n")
	print("encypted text")						
	print("".join(map(str,f)))					
	print("\n\n")
	print("decrypted text")						
	print("".join(map(str,res)))					
	print("\n\n")								
	return res					
						
											
