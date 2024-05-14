from tkinter import *
from PIL import ImageTk
import signin


def login_page():
    root_up.destroy()
    signin.work()


root_up = Tk()
w = 780
h = 500
sw = root_up.winfo_screenwidth()
sh = root_up.winfo_screenheight()

x = (sw // 2) - (w // 2)
y = (sh // 2) - (h // 2)
root_up.geometry(f"{w}x{h}+{x}+{y}")
root_up.configure(bg="black")
root_up.resizable(0, 0)
root_up.title('Sign Up')

photo1 = ImageTk.PhotoImage(file='image/background.jpg')
Label(root_up, image=photo1).pack()

heading = Label(root_up, text='CREATE ACCOUNT', font=('Open Sans', 15, 'bold'), bg='blue', fg='white')
heading.place(x=490, y=60)

email = Label(root_up, text='Email', width=10, font=('Open Sans', 10, 'bold'), bg='white'
              , fg='black')
email.place(x=460, y=100)

emailEntry = Entry(root_up, width=30, font=('Open Sans', 10, 'bold'), bg='white'
                   , fg='black', bd=2)
emailEntry.place(x=480, y=120)

username = Label(root_up, text='Username', width=10, font=('Open Sans', 10, 'bold'), bg='white'
                 , fg='black')
username.place(x=470, y=145)

usernameEntry = Entry(root_up, width=30, font=('Open Sans', 10, 'bold'), bg='white'
                      , fg='black', bd=2)
usernameEntry.place(x=480, y=165)

uni = Label(root_up, text='University', width=10, font=('Open Sans', 10, 'bold'), bg='white'
            , fg='black')
uni.place(x=470, y=190)

uniEntry = Entry(root_up, width=30, font=('Open Sans', 10, 'bold'), bg='white'
                 , fg='black', bd=2)
uniEntry.place(x=480, y=210)

dept = Label(root_up, text='Department', width=10, font=('Open Sans', 10, 'bold'), bg='white'
             , fg='black')
dept.place(x=475, y=235)

deptEntry = Entry(root_up, width=30, font=('Open Sans', 10, 'bold'), bg='white'
                  , fg='black', bd=2)
deptEntry.place(x=480, y=255)

pas = Label(root_up, text='Password', width=10, font=('Open Sans', 10, 'bold'), bg='white'
            , fg='black')
pas.place(x=470, y=280)

pasEntry = Entry(root_up, width=30, font=('Open Sans', 10, 'bold'), bg='white'
                 , fg='black', bd=2)
pasEntry.place(x=480, y=300)

cpas = Label(root_up, text='Confirm Password', width=20, font=('Open Sans', 10, 'bold'), bg='white'
             , fg='black')
cpas.place(x=455, y=325)

cpasEntry = Entry(root_up, width=30, font=('Open Sans', 10, 'bold'), bg='white'
                  , fg='black', bd=2)
cpasEntry.place(x=480, y=345)

login = Button(root_up, text='Sign Up', font=('Open Sans', 14, 'bold'),
               bg='blue', fg='white', bd=0, width=16,command=login_page)
login.place(x=490, y=380)

sign = Label(root_up, text='Already have an account?', font=('Open Sans', 8, 'bold')
             , fg='black', bg='white')
sign.place(x=500, y=420)

login = Button(root_up, text='Login', bd=0, bg='white',
               activebackground='white',
               font=('Open Sans', 9, 'bold',), fg='blue', command=login_page)
login.place(x=650, y=420)

root_up.mainloop()
