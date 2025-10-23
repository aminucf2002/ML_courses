import tkinter as tk   
#%%
 
window=tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

#Label
my_label=tk.Label(text="I am a Label",font=("Arial",24,"bold"))
my_label.pack(side='left')  # Show it onto the screen
my_label['text']="New Text"

#Button


def button_clicked():
    my_label['text']="Button got Clicked"   

button=tk.Button(text="Click Me",command=button_clicked)
button.pack()

#Entry compoenent
input=tk.Entry(width=10)
input.pack()
print(input.get())


mianloop=tk.mainloop()
# %%
