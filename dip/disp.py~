from gamma import *
from Tkinter import *
import numpy as np
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
#from PIL import ImageTk
#from Tkinter import messagebox
from time import sleep
def show():
	v=e1.get()
	lamb(v)
	sleep(5)
	logo=ImageTk.PhotoImage(Image.open("result.png"))
	w1 = Label(master,image=logo)
	w1.grid(row=1,column=1)
master=Tk()
#canvas=Canvas(master,width= 600,height =600 )
#messagebox.showerror("Error","Error message")
#messagebox.showwarning("warning","warning message")
#canvas.pack(o)
pogo=ImageTk.PhotoImage(Image.open("moon.jpg"))

#canvas.create_image(0, 0, anchor=NW, image=logo)
entry=Label(master,text="Enter the gamma value").grid(row=0,column=1)
e1=Entry(master)
e1.grid(row=0,column=1)
w2 = Label(master,image=pogo)

w2.grid(row=1,column=0)
Button(master,text="quit",command=master.quit).grid(row=3,column=0)
Button(master,text="show",command=show).grid(row=3,column=1)
master.mainloop()

