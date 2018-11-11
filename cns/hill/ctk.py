from Tkinter import *
from encrypt import *
enc=[]
def show():
	enc=encrypt(e1.get())
	e="".join(map(str,enc))
	blank.insert(0,e)
master=Tk()
master.title("HILL ENCYPTOR")
First=Label(master,text="message to be encrypted").grid(row=0,column=0)
answer=Label(master,text="encrypted message").grid(row=2,column=0)
e1=Entry(master)
blank=Entry(master)
blank.grid(row=2,column=1)
e1.grid(row=0,column=1)
Button(master,text="quit",command=master.quit).grid(row=3,column=0)
Button(master,text="show",command=show).grid(row=3,column=1)
mainloop()

