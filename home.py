from tkinter import *
from PIL import Image, ImageTk

def contest():
    root_home.destroy()
    import contest
def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    photo = ImageTk.PhotoImage(resized_image)
    return photo


root_home = Tk()
w = 780
h = 550
sw = root_home.winfo_screenwidth()
sh = root_home.winfo_screenheight()
root_home.overrideredirect(True)

x = (sw // 2) - (w // 2)
y = (sh // 2) - (h // 2)
root_home.geometry(f"{w}x{h}+{x}+{y}")
root_home.configure(bg="#E6F5FC")
root_home.resizable(0, 0)
root_home.title('')

label1 = Label(root_home, width=120, height=5, bg='#2E8FC2')
label1.place(x=0, y=0)

home_path = 'image/home-button.png'
home = resize_image(home_path, 40, 40)
homeL = Label(root_home, image=home, bg='#2E8FC2')
homeL.place(x=10, y=20)

heading = Label(root_home, width=30, text='Welcome To UniConnect', font=('Open Sans', 22, 'bold'), bg='#2E8FC2',
                fg='white')
heading.place(x=100, y=20)

label2 = Button(root_home, width=20, height=10, bg='white',command=contest)
label2.place(x=30, y=100)

label3 = Button(root_home, width=20, height=10, bg='white')
label3.place(x=220, y=100)

label4 = Button(root_home, width=20, height=10, bg='white')
label4.place(x=410, y=100)

label5 = Button(root_home, width=20, height=10, bg='white')
label5.place(x=600, y=100)

label6 = Button(root_home, width=20, height=10, bg='white')
label6.place(x=30, y=300)

label7 = Button(root_home, width=20, height=10, bg='white')
label7.place(x=220, y=300)

label8 = Button(root_home, width=20, height=10, bg='white')
label8.place(x=410, y=300)

label9 = Button(root_home, width=20, height=10, bg='white')
label9.place(x=600, y=300)

contest_path = 'image/success.png'
contest = resize_image(contest_path, 80, 80)
CL = Label(root_home, image=contest, bg='white')
CL.place(x=65, y=140)

r_path = 'image/seo.png'
r = resize_image(r_path, 80, 80)
rL = Label(root_home, image=r, bg='white')
rL.place(x=260, y=140)

n_path = 'image/publication.png'
n = resize_image(n_path, 80, 80)
nL = Label(root_home, image=n, bg='white')
nL.place(x=450, y=140)

j_path = 'image/businessman.png'
j = resize_image(j_path, 80, 80)
jL = Label(root_home, image=j, bg='white')
jL.place(x=640, y=140)

q_path = 'image/speech-bubble.png'
q = resize_image(q_path, 80, 80)
qL = Label(root_home, image=q, bg='white')
qL.place(x=65, y=335)

club_path = 'image/membership.png'
club = resize_image(club_path, 80, 80)
clubL = Label(root_home, image=club, bg='white')
clubL.place(x=260, y=335)

exchange_path = 'image/international-relations.png'
exchange = resize_image(exchange_path, 80, 80)
exchangeL = Label(root_home, image=exchange, bg='white')
exchangeL.place(x=450, y=335)

skill_path = 'image/skill.png'
skill = resize_image(skill_path, 90, 90)
skillL = Label(root_home, image=skill, bg='white')
skillL.place(x=640, y=335)


root_home.mainloop()
