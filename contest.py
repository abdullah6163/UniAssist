from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def back():
    root_cont.destroy()
    import home

def register_success():
    messagebox.showinfo("Registration", "Successfully Registered")


def organize():
    root_cont.destroy()
    import organize

root_cont = Tk()
w = 800
h = 530
sw = root_cont.winfo_screenwidth()
sh = root_cont.winfo_screenheight()

x = (sw // 2) - (w // 2)
y = (sh // 2) - (h // 2)
root_cont.geometry(f"{w}x{h}+{x}+{y}")
root_cont.configure(bg="#E6F5FC")
root_cont.resizable(0, 0)
root_cont.title('Contest Page')

def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    photo = ImageTk.PhotoImage(resized_image)
    return photo

label1 = Label(root_cont, width=120, height=5, bg='#2E8FC2')
label1.place(x=0, y=0)

previous_path = 'image/previous.png'
previous = resize_image(previous_path, 40, 40)
previousL = Button(root_cont, image=previous, bg='#2E8FC2',bd=0,activebackground='#2E8FC2',command=back)
previousL.place(x=30, y=20)

heading = Label(root_cont, width=30, text='Contest', font=('Open Sans', 22, 'bold'), bg='#2E8FC2', fg='white')
heading.place(x=100, y=20)

running = Label(root_cont, width=30, text='Running Contest', font=('Open Sans', 22, 'bold'), bg='#5AE684', fg='black')
running.place(x=100, y=100)

heading1 = Label(root_cont, width=60, text='1. Diu Coding Challenge (Running, 15 May 2024, Duration: 2 hours)',
                 font=('Open Sans', 12, ),bg='#E6F5FC', fg='black')
heading1.place(x=60, y=150)

heading2 = Label(root_cont, width=60, text='2. Aiub Programming Contest (Running, 15 May 2024, Duration: 2 hours)',
                 font=('Open Sans', 12, ),bg='#E6F5FC', fg='black')
heading2.place(x=80, y=180)

heading3 = Label(root_cont, width=60, text='3. Du Beginner Contest (Running, 15 May 2024, Duration: 2 hours)',
                 font=('Open Sans', 12, ),bg='#E6F5FC', fg='black')
heading3.place(x=60, y=210)

button1 = Button(root_cont,width=8,height=0,text="Join",font=('Open Sans',8),bg='#20C5CA',fg='black')
button1.place(x=650,y=150)

button2 = Button(root_cont,width=8,height=0,text="Join",font=('Open Sans',8),bg='#20C5CA',fg='black')
button2.place(x=650,y=180)

button3 = Button(root_cont,width=8,height=0,text="Join",font=('Open Sans',8),bg='#20C5CA',fg='black')
button3.place(x=650,y=210)

upcoming = Label(root_cont, width=30, text='Upcoming Contest', font=('Open Sans', 22, 'bold'), bg='#5AE684', fg='black')
upcoming.place(x=100, y=250)

heading4 = Label(root_cont, width=60, text='1. Algorithm Hackathon (Running, 15 May 2024, Duration: 2 hours)',
                 font=('Open Sans', 12, ),bg='#E6F5FC', fg='black')
heading4.place(x=60, y=300)

heading5 = Label(root_cont, width=60, text='2. Data Science Competition (Running, 15 May 2024, Duration: 2 hours)',
                 font=('Open Sans', 12, ),bg='#E6F5FC', fg='black')
heading5.place(x=80, y=330)

button4 = Button(root_cont,width=8,height=0,text="Register",font=('Open Sans',8),bg='#20C5CA',fg='black', command=register_success)
button4.place(x=650,y=290)

button5 = Button(root_cont,width=8,height=0,text="Register",font=('Open Sans',8),bg='#20C5CA',fg='black', command=register_success)
button5.place(x=650,y=320)

heading6 = Label(root_cont, width=60, text='Want to organize a Contest?',
                 font=('Open Sans', 12, 'bold'),bg='#E6F5FC', fg='black')
heading6.place(x=80, y=450)

button6 = Button(root_cont,width=8,height=0,text="Click Here",font=('Open Sans',12,'bold'),bg='#E6F5FC',fg='blue',bd=0,command=organize)
button6.place(x=500,y=448)

root_cont.mainloop()
