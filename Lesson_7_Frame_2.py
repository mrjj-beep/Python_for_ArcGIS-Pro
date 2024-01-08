from tkinter import *

class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)

        # self.myCanvas = Canvas()
        self.myCanvas = Canvas(width=300, height=200, bg="blue")
        self.myCanvas.grid()
        self.myCanvas.create_rectangle(10, 10, 100, 100, outline="red", fill="green", width=5)
        self.myCanvas.create_oval(10, 55, 100, 100, outline="white", fill="purple", width=2)
        self.myCanvas.create_line(10, 100, 100, 10, fill="orange", width=3, arrow = "both")
        self.myCanvas.create_rectangle(110, 10, 200, 100, outline="red", fill="green", width=5)
        self.myCanvas.create_oval(110, 10, 200, 55, outline="white", fill="purple", width=2)
        self.myCanvas.create_line(110, 10, 200, 100, fill="orange", width=3, arrow = "last")
        self.myCanvas.create_oval(10, 50, 100, 100, outline="white", fill="purple", width=2)
        self.myCanvas.create_text(55, 30, text="Здрасте!", justify="center",  width=90, font="Times", fill="white")
        
# Now create a MyFrame object and call on mainloop
frame02 = MyFrame()
frame02.mainloop()

