from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("300x200")
        self.master.title("Text Sampler")
        self.grid()

        self.sample_label = Label(self, text="Some Sample Text", font = "Courier 10")
        self.sample_label.grid(row = 0, column = 0, columnspan = 2)

        self.bold_on = IntVar()
        self.check_bold = Checkbutton(self, text = "Bold",
                variable = self.bold_on, command = self.set_font)
        self.check_bold.grid(row = 1, column = 0)

        self.underline_on = IntVar()
        self.check_underline = Checkbutton(self, text = "Underline",
                variable = self.underline_on, command = self.set_font)
        self.check_underline.grid(row = 1, column = 1)

    def set_font(self):
        new_font = "Courier 10"

        if self.bold_on.get() == 1:
            new_font = new_font + " bold"

        if self.underline_on.get() == 1:
            new_font = new_font + " underline"
       
        self.sample_label.config( font = new_font)

frame06 = MyFrame()
frame06.mainloop()
