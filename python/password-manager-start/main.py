from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manger")

canvas = Canvas(height=200,width =200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image= logo_img)
canvas.grid(row=0,column=1)

website_label = Label(text="website")
website_label.grid(row=1)
email_label = Label(text="email")
email_label.grid(row=2)
password_label = Label(text="password")
password_label.grid(row=3)

website_entry = Entry(width=35)
website_entry.grid(row=1.column=1)

window.mainloop()
