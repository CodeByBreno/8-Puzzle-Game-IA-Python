from tkinter import *
import tkinter.font as tkFont
    
app = Tk()
app.geometry("600x500")

def decreaseSize():
    buttonExample1.configure(height = 100,
                             width = 100)

def increaseSize():
    buttonExample2.configure(height = 400,
                             width = 400)

pixelVirtual = PhotoImage(width=1, height=1)
    
buttonExample1 = Button(app,
                           text="Decrease Size",
                           background="#224455",
                           image=pixelVirtual,
                           width=200,
                           height=200,
                           compound="c",
                           font=("Arial", 20),
                           command = decreaseSize)
buttonExample2 = Button(app,
                           text="Increase Size",
                           background="#113377",
                           image=pixelVirtual,
                           width=200,
                           height=200,
                           compound=CENTER,
                           font=("Arial", 20),
                           command = increaseSize)

buttonExample1.grid(column=0, row=1)
buttonExample2.grid(column=2, row=1)
app.mainloop()
