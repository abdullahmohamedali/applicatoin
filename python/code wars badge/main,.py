import tkinter as tk
from PIL import Image
import imagetk
import requests
from io import BytesIO

URL = "https://www.codewars.com/users/abdullah%20programer/badges/large"

def get_image(url):
    response = requests.get(url)
    img_data = BytesIO(response.content)
    img = Image.open(img_data)
    return imagetk.PhotoImage(img)

root = tk.Tk()
root.title("Codewars Badge")
root.attributes("-topmost", True)
root.geometry("+10+10")  # Position the window at x=10, y=10

img = get_image(URL)
panel = tk.Label(root, image=img)
panel.pack(side="top", fill="both", expand="yes")

root.mainloop()
