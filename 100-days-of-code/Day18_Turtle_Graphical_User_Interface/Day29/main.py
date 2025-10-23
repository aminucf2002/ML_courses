from tkinter import *
from PIL import ImageTk, Image

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP -------------------------------
window = Tk()
window.title("Password Manager")
canvas = Canvas(height=200, width=200)
img = Image.open("logo.png")
logo_img = ImageTk.PhotoImage(img)
canvas.create_image(100, 100,image=logo_img)
window.config(padx=50, pady=50)

canvas.pack()


window.mainloop()