# display a window with a button
import tkinter
from tkinter import *
from tkinter import ttk #only for combobox
# from PIL import ImageTk, Image
class Window2():
    def __init__(self):
        window = Tk()
        window.title("Window-2")
        window.geometry("300x400")
        window.resizable(False, False)
        # add label
        lblCollege = Label(window, text="PCPS College")
        lblCollege.place(x=40, y=30)

        # add entry - text box - single line
        txtName = Entry(window, width = 20)
        txtName.place(x=20, y=60)

        # add password box
        txtPass = Entry (window, width=20, show='*')
        txtPass.place(x=20, y=90)

        # text-comment box/text area
        txtComments = Text(window, width= 30, height=3)
        txtComments.place(x=20, y=120)

        # radio button - single selection from multiple options
        rb1 = Radiobutton(window, text="Option-1", value='v1')
        rb2 = Radiobutton(window, text="Option-2", value='v2')
        rb1.place(x=20, y=180)
        rb2.place(x=20, y=200)

        #checkbutton - check box (Select multiple values from multiple options"
        ck1 = Checkbutton(window, text="Option-1")
        ck2 = Checkbutton(window, text="Option-2")
        ck3 = Checkbutton(window, text="Option-3")
        ck1.place(x=20, y=220)
        ck2.place(x=20, y=240)
        ck3.place(x=20, y=260)

        cmb1 = ttk.Combobox(window)
        cmb1['values'] = ('Value1', 'Value2', 'Value3')
        cmb1.place(x=20, y=300)

        # canvas - image viewer
        # pip install pillow
        # from PIL import ImageTk, Image
        # tmpImage = Image.open('paint.png')
        # imgFile = ImageTk.PhotoImage(tmpImage)
        # canvas = Canvas(window, width=150, height=50)
        # canvas.create_image(0,0, image=imgFile)
        # canvas.place(x=20, y=360)

        # button
        btnSave = Button(window, text="SAVE")
        btnSave.place(x=20, y=350)


        window.mainloop()