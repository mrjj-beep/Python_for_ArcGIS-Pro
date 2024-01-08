try:
   infile = open('C:\Users\MrJoh\OneDrive\Documents\TXST\Python\Lesson 11\myfile.txt', 'r')
   infile.write("Hello")

   infile.close()
except IOError as ioe:
   print (ioe.filename)
   print (ioe.strerror)
