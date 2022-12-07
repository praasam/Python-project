from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Validation Test")
window.geometry("350x400")
window.resizable(False, False)

lbl1 = Label(window, text="ID")
lbl1.place(x=40, y=20)

ID = ttk.Combobox(window)
ID['values'] = ('Value1', 'Value2', 'Value3')
ID.place(x=40, y=40)

btnSave = Button(window, text="SAVE")
btnSave.place(x=75, y=75)

btnClose = Button(window, text="CLOSE")
btnClose.place(x=150, y=75)

window.mainloop()