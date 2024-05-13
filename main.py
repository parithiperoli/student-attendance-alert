from tkinter import *
from PIL import ImageTk,Image
import tkinter



window=tkinter.Tk()
window.geometry("700x600")
window.title("student_attentive")
class sample:
    name="guru"
    text="Student Attentive"

image_0=Image.open('static/class.jpg')
bck_end=ImageTk.PhotoImage(image_0)

def login():
    window.destroy()
    import log
def register():
    window.destroy()
    import register


canvas = tkinter.Canvas(window,  width=1550, height=900)
canvas.pack()
canvas.create_image(-10,-3,anchor=NW,image=bck_end)

canvas.create_text(350,100,text=sample.text,font=('times', 50, ' bold '),fill="#0179F8")


txt=Button(window,width=10,height=0,text="Login",fg="white",bg="#334CAF",font=('times', 15, ' bold '),command=login)
txt.place(x=150,y=450)
txt=Button(window,width=10,height=0,text="Register",fg="white",bg="#334CAF",font=('times', 15, ' bold '),command=register)
txt.place(x=400,y=450)


window.mainloop()
