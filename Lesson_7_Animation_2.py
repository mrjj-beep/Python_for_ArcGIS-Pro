from tkinter import *
from time import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)

        # self.myCanvas = Canvas()
        self.myCanvas = Canvas(width=250, height=250, bg="light blue")
        self.myCanvas.grid()

        self.myCanvas.create_oval(100, 102.5, 225, 227.5, outline = "red", fill = "red")
        self.myCanvas.create_oval(106, 108.5, 219, 221.5, outline = "orange", fill = "orange")
        self.myCanvas.create_oval(112, 114.5, 213, 215.5, outline = "yellow", fill = "yellow")
        self.myCanvas.create_oval(118, 120.5, 207, 209.5, outline = "green", fill = "green")
        self.myCanvas.create_oval(124, 126.5, 201, 203.5, outline = "blue", fill = "blue")
        self.myCanvas.create_oval(130, 132.5, 195, 197.5, outline = "purple", fill = "purple")
        self.myCanvas.create_oval(136, 138.5, 189, 191.5, outline = "light blue", fill = "light blue")        
        self.myCanvas.create_rectangle(0, 165, 250, 250, fill = "dark green")

        self.myCanvas.create_text(125, 75, anchor = "center", text = "Кто хочет играть в Понг?", font = "Times", fill = "red")

        my_rect_id = self.myCanvas.create_rectangle(10, 10, 50, 50, fill = "white")
        self.myCanvas.update()

        for count in range(10):
            increment = 10*count
            self.myCanvas.coords(my_rect_id, 10 + increment, 10 + increment, 50 + increment, 50 + increment)
            self.myCanvas.update()
            sleep(0.1)

        for count in range(10):
            increment = 10*count
            self.myCanvas.coords(my_rect_id, 100 + increment, 100 - increment, 140 + increment, 140 - increment)
            self.myCanvas.update()
            sleep(0.1)

        for count in range(20):
            increment = 10*count
            self.myCanvas.coords(my_rect_id, 200 - increment, 10 + increment, 240 - increment, 50 + increment)
            self.myCanvas.update()
            sleep(0.1)

        for count in range(20):
            increment = 10*count
            self.myCanvas.coords(my_rect_id, 10, 200 - increment, 50, 240 - increment)
            self.myCanvas.update()
            sleep(0.1)

# Now create a MyFrame object and call on mainloop
frame02 = MyFrame()
frame02.mainloop()
