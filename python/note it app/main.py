import tkinter
import customtkinter
import sqlite3
import json

db = sqlite3.connect("app.db")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("500x500")
app.title("note app")
note_var = ""


def save():
    db.execute(f"insert into skills (note) values('{note_var}')")
    


def add_note():
    entry = customtkinter.CTkEntry(app, width=150 , height=40, textvariable=note_var)
    entry.pack()
    entry.place(y = 50, x = 50)
    print(note_var)
    db.execute(f"insert into skills (note) values('{note_var}')")








button = customtkinter.CTkButton(app, text="add note", command=add_note)
button.pack()
button.place(y= 450, x= 50)
button1 = customtkinter.CTkButton(app, text="save", command=save)
button1.pack()
button1.place(y= 450, x= 350)
button = customtkinter.CTkButton(app, text="remove note")
button.pack()
button.place(y= 450, x= 200)




app.mainloop()




