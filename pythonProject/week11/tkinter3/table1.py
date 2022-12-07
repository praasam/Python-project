from tkinter import *
from tkinter import ttk

window = Tk()
window.geometry("450x350")
window.resizable(False, False)
window.title("Data Table Demo")

frame1 = Frame(window)
frame1.pack()

tblPersons = ttk.Treeview(frame1)
tblPersons['columns']=('pid', 'name', 'address')

tblPersons.column("#0", width=0, stretch=NO)
tblPersons.column("pid", width=50, anchor=CENTER)
tblPersons.column("name", width=100, anchor=CENTER)
tblPersons.column("address", width=150, anchor=CENTER)

tblPersons.heading("#0", text="", anchor=CENTER)
tblPersons.heading("pid", text="ID", anchor=CENTER)
tblPersons.heading("name", text="NAME", anchor=CENTER)
tblPersons.heading("address", text="ADDRESS", anchor=CENTER)

# Add record
tblPersons.insert(parent='', index='end', iid=0, values=(1, 'Aasma', 'KTM'))
tblPersons.insert(parent='', index='end', iid=1, values=(2, 'Deeshri', 'KTM'))

tblPersons.pack()


window.mainloop()
