from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def save():
    # read text from textbox
    strID = txtID.get()
    if strID.isnumeric():
        tmpID = int(strID)  #string to int
        if tmpID>=1 and tmpID<=99:
            messagevox.showinfo("Title", "Valid ID")
        else:
            messagebox.showinfo("Title", "ID out of range")
    else:
        messagebox.showinfo("Title", "Invalid data type")

window = Tk()
window.title("Validation Test")
window.geometry("350x400")
window.resizable(False, False)

lblID = Label(window, text="ID: ")
lblID.place(x=20, y=20)

txtID = Entry(window, width=15)
txtID.place(x=75, y=20)

btnSave = Button(window, text="SAVE", command=save)
btnSave.place(x=75, y=75)

btnClose = Button(window, text="CLOSE")
btnClose.place(x=150, y=75)

window.mainloop()

# print(help(str))