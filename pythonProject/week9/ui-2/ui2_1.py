# pip install tk

from tkinter import Tk
from tkinter.ttk import Label
from tkinter import ttk

window = Tk()   #declare and initialize
window.geometry("250x350") #Resize
window.resizable(False, False)    #resizable -> false
window.title("Main Window")    #title change
label = Label(window, text='This ia a Label')
label = ttk.Label(
    window,
    text='A Label with the Times New Roman font',
    font=("Times New Roman", 10))
label.pack()
window.mainloop()   #display















#Resize window

