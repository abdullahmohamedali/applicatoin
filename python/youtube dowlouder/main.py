import tkinter
import customtkinter
from pytube import YouTube

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def start_dowloud():
        ytlink = link.get()
        ytobjects = YouTube(ytlink)
        vidio = ytobjects.streams.get_by_resolution()
        vidio.download()


app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downlouder")

title = customtkinter.CTkLabel(app, text="insert a youtube dowlouder")
title.pack(padx = 10, pady = 10)

url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height= 40, textvariable=url_var)
link.pack()

dowloud = customtkinter.CTkButton(app, text = "dowloud", command= start_dowloud)
dowloud.pack()

app.mainloop()