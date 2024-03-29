from tkinter import *

class MyFrame (Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry ("350x200")
        self.master.title ("Lesson 12 Assignment")
        self.grid()

        self.prompt = Label (self, text = "Enter your text: ")
        self.prompt.grid (row = 0, column = 0)

        self.input = Entry (self)
        self.input.grid (row = 0, column = 1)

        self.button_submit = Button(self, text = "Submit", command = self.submit_click)
        self.button_submit.grid (row = 0, column = 2)

        # Display text here
        self.my_text = StringVar()
        self.my_text.set ("Enter text above: ")
        self.message = Label (self, textvariable = self.my_text, font = "Arial 8")
        self.message.grid (row = 1, columnspan = 3, pady = 20)

        # Options
        self.bold_on = IntVar()
        self.check_bold = Checkbutton(self, text = "Bold", variable = self.bold_on, command = self.set_font)
        self.check_bold.grid(row = 2, column = 0)

        self.underline_on = IntVar()
        self.check_underline = Checkbutton(self, text = "Underline", variable = self.underline_on, command = self.set_font)
        self.check_underline.grid(row = 2, column = 1)

        # Font sizes
        self.point_size = StringVar()
        self.point_size.set("8")
        self.eight_point = Radiobutton(self, text = "8 point", variable = self.point_size, value = "8", command = self.set_font)
        self.eight_point.grid(row = 3, column = 0)

        self.ten_point = Radiobutton(self, text = "10 point", variable = self.point_size, value = "10", command = self.set_font)
        self.ten_point.grid(row = 3, column = 1)

        self.twelve_point = Radiobutton(self, text = "12 point", variable = self.point_size, value = "12", command = self.set_font)
        self.twelve_point.grid(row = 3, column = 2)


    def set_font(self):
        new_font = "Arial"

        if self.point_size.get() == "8":
            new_font = new_font + "8"
        elif self.point_size.get() == "10":
            new_font = new_font + "10"
        else:
            new_font = new_font + "12"

        if self.bold_on.get() == 1:
            new_font = new_font + "bold"

        if self.underline_on.get() == 1:
            new_font = new_font + "underline"
    
        self.message.config (font = new_font)

    def submit_click(self):
        self.my_text.set(self.input.get())


frame12 = MyFrame()
frame12.mainloop()


        

        
