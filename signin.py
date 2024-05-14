from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def work():

    def home():
        user = username.get()
        pas = password.get()
        if user == 'admin' and pas == '1234':
            root.destroy()
            import home
        elif user == 'admin' and pas == '1234':
            messagebox.showerror("Invalid", "Invalid username or password")
        elif user != 'admin':
            messagebox.showerror("invalid", "Invalid username")
        elif pas != '1234':
            messagebox.showerror("Invalid", 'Invalid Password')



    def sign_up():
        root.destroy()
        import signup

    def hide():
        open.config(file='image/closeye.png')
        password.config(show='*')

    def on_enter(event):
        if username.get() == 'Username':
            username.delete(0, END)

    def on_enter2(event):
        if password.get() == 'Password':
            password.delete(0, END)

    root = Tk()
    w = 780
    h = 500

    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()

    x = (sw // 2) - (w // 2)
    y = (sh // 2) - (h // 2)
    root.geometry(f"{w}x{h}+{x}+{y}")
    root.configure(bg="black")
    root.resizable(0, 0)
    root.title('Login Page')

    photo1 = ImageTk.PhotoImage(file='image/background.jpg')
    Label(root, image=photo1).pack()

    heading = Label(root, text='USER LOGIN', font=('Open Sans', 20, 'bold'), bg='blue', fg='white')
    heading.place(x=520, y=60)

    username = Entry(root, width=15, font=('Microsoft Yahei UI Light', 10, 'bold'), bd=0, fg='black')
    username.place(x=510, y=120)
    username.insert(0, 'Username')
    username.bind('<FocusIn>', on_enter)

    Frame(root, width=200, height=2, bg='black').place(x=510, y=140)

    password = Entry(root, width=15, font=('Microsoft Yahei UI Light', 10, 'bold'), bd=0, fg='black')
    password.place(x=510, y=160)
    password.insert(0, 'Password')
    password.bind('<FocusIn>', on_enter2)

    Frame(root, width=200, height=2, bg='black').place(x=510, y=180)

    open = PhotoImage(file='image/openeye.png')
    eyebutton = Button(root, image=open, bd=0, bg='white',
                       activebackground='white', command=hide)
    eyebutton.place(x=680, y=150)

    forget = Button(root, text='Forget Password?', bd=0, bg='white',
                    activebackground='white',
                    font=('Microsoft Yahei UI light', 9, 'bold'))
    forget.place(x=600, y=190)

    login = Button(root, text='Login', font=('Open Sans', 14, 'bold'),
                   bg='blue', fg='white', bd=0, width=16,command=home)
    login.place(x=510, y=250)

    orr = Label(root, text='-----------------OR-----------------', font=('Open Sans', 12, 'bold')
                , fg='black', bg='white')
    orr.place(x=510, y=300)

    fb = PhotoImage(file='image/facebook.png')
    fbL = Label(root, image=fb, bg='white')
    fbL.place(x=550, y=350)

    tw = PhotoImage(file='image/twitter.png')
    twL = Label(root, image=tw, bg='white')
    twL.place(x=600, y=350)

    g = PhotoImage(file='image/google.png')
    gL = Label(root, image=g, bg='white')
    gL.place(x=650, y=350)

    sign = Label(root, text='Dont have any account?', font=('Open Sans', 8, 'bold')
                 , fg='black', bg='white')
    sign.place(x=510, y=400)

    cr = Button(root, text='Crete a new', font=('Open Sans', 8, 'bold')
                , fg='blue', bg='white', activebackground='white', bd=0, command=sign_up)
    cr.place(x=650, y=400)

    root.mainloop()


if __name__ == "__main__":
    work()
