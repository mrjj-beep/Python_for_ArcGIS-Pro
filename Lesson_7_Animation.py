from tkinter import *
from time import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)

        # self.myCanvas = Canvas()
        self.myCanvas = Canvas(width=300, height=200, bg="white")
        self.myCanvas.grid()

        self.myCanvas.create_text(150, 100, anchor = "center", text = "Кто хочет играть в Понг?", font = "Times", fill = "red")

        self.myCanvas.create_rectangle(10, 10, 50, 50)
        self.myCanvas.update()

        for count in range(10):
            increment = 10*count
            self.myCanvas.create_rectangle(10 + increment, 10 + increment, 50 + increment, 50 + increment)
            self.myCanvas.update()
            sleep(0.2)

        # Now color over the previous rectangle
            self.myCanvas.create_rectangle(10 + increment, 10 + increment, 50 + increment, 50 + increment, outline="white")
            self.myCanvas.update()
            sleep(0.2)

# Now create a MyFrame object and call on mainloop
frame02 = MyFrame()
frame02.mainloop()
