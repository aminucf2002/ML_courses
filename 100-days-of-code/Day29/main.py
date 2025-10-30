from tkinter import *
import os
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP -------------------------------
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
#canvas
canvas = Canvas(height=200, width=200)
script_dir=os.path.dirname(__file__)
image_path=os.path.join(script_dir,'logo.png')
logo_img=PhotoImage(file=image_path)
#logo_img = PhotoImage(file="C:/Users/pc/Documents/Git Repositories/ML_courses/ML_courses/100-days-of-code/Day29/logo.png")
canvas.create_image(100, 100,image=logo_img)
canvas.grid(row=0, column=1)
#labels
window.config(padx=20, pady=20)
website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
password_label=Label(text="Password:")  
password_label.grid(row=3,column=0)     
email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)            

#entries
website_entry=Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

#bottons
generate_password_button=Button(text="Generate Password")
generate_password_button.grid(row=3,column=2)
add_button=Button(text="Add",width=36)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()