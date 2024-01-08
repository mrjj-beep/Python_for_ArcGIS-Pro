# Entry Component

from tkinter import *

class MyFrame(Frame):
   def __init__(self):
       Frame.__init__(self)
       self.master.geometry("300x200")
       self.master.title("My GUI")
       self.grid()

       self.prompt = Label(self, text = "What's your name?")
       self.prompt.grid()

       self.input = Entry(self)
       self.input.grid()

       self.button_submit = Button( self, text = "Submit",
           command = self.submit_click )
       self.button_submit.grid()

       self.my_text = StringVar()
       self.message = Label(self, textvariable = self.my_text)
       self.message.grid()

   def submit_click(self):
       output_message = "Hi " + self.input.get()
       self.my_text.set(output_message)

frame04 = MyFrame()
frame04.mainloop()
