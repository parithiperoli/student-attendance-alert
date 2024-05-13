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


def student():
    window.destroy()
    import student_reg

def login():

      window.destroy()
      import not_attentive

def back():
    window.destroy()
    import main
def video():
  window.destroy()
  import video


canvas = tkinter.Canvas(window,  width=1550, height=900)
canvas.pack()
canvas.create_image(-10,-3,anchor=NW,image=bck_end)






txt=Button(window,width=15,height=1,text="Student Register",fg="white",bg="#334CAF",font=('times', 15, ' bold '),command=student)
txt.place(x=250,y=150)
txt=Button(window,width=15,height=1,text="Not Attentive student",fg="white",bg="#334CAF",font=('times', 15, ' bold '),command=login)
txt.place(x=250,y=245)
txt=Button(window,width=15,height=1,text="VIDEO",fg="white",bg="#334CAF",font=('times', 15, ' bold '),command=video)
txt.place(x=250,y=345)



window.mainloop()
