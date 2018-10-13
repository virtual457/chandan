from Tkinter import *
master=Tk()
master.title("Some RANdom Db")
def insert():
	print("this is function insert")
	root=Tk()
	text2=Label(root,text="you have sucessfully opened").grid(row=0,column=0)
def show():
	print("this as function show")
def dele():
	print("this is function delete")
def first():
	print("this is function first")
def prev():
	print("this is function prev")
def nest():
	print("this is function next")
def last():
	print("this is function last")
text1=Label(master,text="whatever u want")
e1=Entry(master).grid(row=1,column=0)
e2=Entry(master).grid(row=2,column=0)
Button(master,text="INSE",command=insert).grid(row=1,column=5)
Button(master,text="SHOW",command=show ).grid(row=2,column=5)
Button(master,text="DELE",command=dele).grid(row=3,column=5)
Button(master,text="FIRST",command=first).grid(row=5,column=1)
Button(master,text="PREV",command=prev).grid(row=5,column=2)
Button(master,text="NEXT",command=nest).grid(row=5,column=3)
Button(master,text="LAST",command=last).grid(row=5,column=4)
Button(master,text="QUIT",command=master.quit).grid(row=4,column=5)
mainloop()
