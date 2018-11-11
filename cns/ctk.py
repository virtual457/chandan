from Tkinter import *
from exa import *
enc=[]
def show():
	public ,private,res,chan=enc(e1.get(),e2.get(),e3.get())
	blank1.insert(0,public)
	blank2.insert(0,private)
	res="".join(map(str,res))
	blank3.insert(0,res)
master=Tk()
master.title("RSA encryptor/decryptor")
First=Label(master,text="enter the first prime number").grid(row=0,column=0)
last=Label(master,text="enter the second prime number").grid(row=1,column=0)
first3=Label(master,text="mesage to be encrypted").grid(row=2,column=0)
first4=Label(master,text="public key").grid(row=3,column=0)
first5=Label(master,text="private key").grid(row=4,column=0)
first6=Label(master,text="encrypted message").grid(row=5,column=0)
first7=Label(master,text="decrypted message").grid(row=6,column=0)


e1=Entry(master)
e2=Entry(master)
e3=Entry(master)
blank1=Entry(master)
blank1.grid(row=3,column=1)
blank2=Entry(master)
blank2.grid(row=4,column=1)
blank3=Entry(master)
blank3.grid(row=5,column=1)
blank4=Entry(master)
blank4.grid(row=6,column=1)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)
Button(master,text="quit",command=master.quit).grid(row=7,column=0)
Button(master,text="show",command=show).grid(row=7,column=1)
mainloop()

