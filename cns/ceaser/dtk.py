from Tkinter import *
from decrypt import *
enc=[]
def show():
	enc=decrypt(e1.get(),e2.get())
	e="".join(map(str,enc))
	blank.insert(0,e)
master=Tk()
master.title("ceaser decryptor")
First=Label(master,text="enter the key").grid(row=0,column=0)
Last=Label(master,text="message to be decrypted").grid(row=1,column=0)
answer=Label(master,text="decrypted message").grid(row=2,column=0)
e1=Entry(master)
e2=Entry(master)
blank=Entry(master)
blank.grid(row=2,column=1)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
Button(master,text="quit",command=master.quit).grid(row=3,column=0)
Button(master,text="show",command=show).grid(row=3,column=1)
mainloop()