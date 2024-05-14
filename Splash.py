from tkinter import *
from PIL import Image, ImageTk
import signin

sp_root = Tk()
width = 700
height = 480
sp_root.overrideredirect(True)

screen_width = sp_root.winfo_screenwidth()
screen_height = sp_root.winfo_screenheight()

x = (screen_width // 2) - (width // 2)
y = (screen_height // 2) - (height // 2)
sp_root.geometry(f"{width}x{height}+{x}+{y}")
sp_root.resizable(0,0)

photo = ImageTk.PhotoImage(file='image/Capture1.PNG')
Label(sp_root, image=photo).pack()

loading_label = Label(sp_root, text="Loading..............", font=("Helvetica", 20), bg="white", fg="black")
loading_label.place(relx=0.5, rely=0.95, anchor=S)


def sign_up():
    sp_root.destroy()
    signin.work()


sp_root.after(4000, sign_up)
sp_root.mainloop()
