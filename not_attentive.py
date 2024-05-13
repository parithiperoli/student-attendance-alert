import os
from tkinter import *
from tkinter import ttk

from PIL import ImageTk,Image
import tkinter



not_attentive_root=tkinter.Tk()
not_attentive_root.geometry("700x600")
not_attentive_root.title("not_attentive")
class sample:
    name="ar_master"
    text="Student Attentive"

image_0=Image.open('static/class.jpg')
bck_end=ImageTk.PhotoImage(image_0)


def selectItem(a):
    curItem = tree.focus()
    data = (tree.item(curItem))
    data1 = (data['values'])
    file_name=(data1[0])
    print(file_name)


    TableMargin = Frame(not_attentive_root, width=500)
    TableMargin.place(x=300, y=110, width=250, height=320)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree1 = ttk.Treeview(TableMargin, columns=("Student"), height=400, selectmode="extended", yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree1.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree1.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree1.heading('Student', text="Student", anchor=W)
    tree1.bind('<ButtonRelease-1>', selectItem)
    tree1.column('#0', stretch=NO, minwidth=100, width=0)
    tree1.pack()
    my_conn = []

    file_path=os.path.join("attentive",file_name)
    file1 = open(file_path, 'r')
    Lines = file1.readlines()
    for line in Lines:
        my_conn.append(str(line))

    for hr_addsalary in my_conn:
        tree1.insert("", 0, values=hr_addsalary)
    tree1.pack()

canvas = tkinter.Canvas(not_attentive_root,  width=1550, height=900)
canvas.pack()
canvas.create_image(-10,-3,anchor=NW,image=bck_end)
canvas.create_text(350,50,text=sample.text,font=('times', 40, ' bold '),fill="#0179F8")
TableMargin = Frame(not_attentive_root, width=500)
TableMargin.place(x=50, y=110,width=220, height=320)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("Date"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Date', text="Date", anchor=W)
tree.bind('<ButtonRelease-1>', selectItem)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.pack()
my_conn=[]
for filename in os.listdir('attentive'):
   my_conn.append(""+filename)
for  hr_addsalary  in my_conn:
    tree.insert("", 0, values=hr_addsalary)
tree.pack()
not_attentive_root.mainloop()
