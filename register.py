from tkinter import *
from PIL import ImageTk,Image
import tkinter

import ar_master

mm = ar_master.master_flask_code()

window=tkinter.Tk()
window.geometry("700x600")
window.title("student_attentive")
class sample:
    name="guru"

image_0=Image.open('static/class.jpg')
bck_end=ImageTk.PhotoImage(image_0)

def register():

    enry1=entry1.get()
    enry2 = entry2.get()
    enry3 = entry3.get()
    maxin = mm.find_max_id("staff_details")
    qry = ("insert into staff_details values('" + str(maxin) + "','" + str(enry1) + "','" + str(
        enry2) + "','" + str(enry3) + "')")
    result = mm.insert_query(qry)
    print(qry)
    window.destroy()
    import main



canvas = tkinter.Canvas(window,  width=1550, height=900)
canvas.pack()
canvas.create_image(-10,-3,anchor=NW,image=bck_end)

canvas.create_text(230,180,text="Name",font=('times', 15, ' bold '),fill="white")

canvas.create_text(230,250,text="Class",font=('times', 15, ' bold '),fill="white")

canvas.create_text(230,330,text="Email",font=('times', 15, ' bold '),fill="white")

entry1=Entry(window,width=20,font=('times', 15, ' bold '))
entry1.place(x=320,y=165)
entry2=Entry(window,width=20,font=('times', 15, ' bold '))
entry2.place(x=320,y=240)
entry3=Entry(window,width=20,font=('times', 15, ' bold '))
entry3.place(x=320,y=315)

txt=Button(window,width=10,height=0,text="Register",fg="white",bg="#334CAF",font=('times', 15, ' bold '),command=register)
txt.place(x=270,y=400)


window.mainloop()
