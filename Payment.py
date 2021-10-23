from tkinter import *
from PIL import ImageTk,Image
root = Tk()
canvas = Canvas(root, width = 500, height = 800)
canvas.pack()
im = Image.open("GoogleQR.jpg")
resize_im = im.resize((180,180), Image.ANTIALIAS)
new_im = ImageTk.PhotoImage(resize_im)
canvas.create_image(20, 20, anchor = NW, image = new_im)
root.mainloop()
