import tkinter

window = tkinter.Tk()
window.title("gui")
window.minsize(500, 300)


my_label = tkinter.Label(text ="new",font=("Areil", 24, "italic"))
my_label.pack()

window.mainloop()