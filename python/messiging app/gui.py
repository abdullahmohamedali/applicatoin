from tkinter import *

app = Tk()
app.geometry("500x500")
app.title("white board ")

e = Entry(width=50)
e.pack()
e.place(x=0,y=450)

botton = Button(app,text="send")

mainloop()