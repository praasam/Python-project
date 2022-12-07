# display a window with a button
import tkinter
from tkinter import *
from window2 import Window2

def displayWin2():
    Window2()  #call __init__() function
window = Tk()
window.geometry("350x400")
window.resizable(False, False)
btnWin2 = Button(text="Window-2", command=displayWin2)
btnWin2.place(x=20, y=20)
window.title("Window-1")

window.mainloop()
