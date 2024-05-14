from tkinter import *
from PIL import Image, ImageTk



def research():
    root_home.destroy()
    import research



def cont():
    root_home.destroy()
    import contest


def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    photo = ImageTk.PhotoImage(resized_image)
    return photo


root_home = Tk()
w = 800
h = 530
sw = root_home.winfo_screenwidth()
sh = root_home.winfo_screenheight()

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

label2 = Button(root_home, width=20, height=10, bg='white', bd=0)
label2.place(x=30, y=100)

label3 = Button(root_home, width=20, height=10, bg='white', bd=0)
label3.place(x=220, y=100)

label4 = Button(root_home, width=20, height=10, bg='white', bd=0)
label4.place(x=410, y=100)

label5 = Button(root_home, width=20, height=10, bg='white', bd=0)
label5.place(x=600, y=100)

label6 = Button(root_home, width=20, height=10, bg='white', bd=0)
label6.place(x=30, y=300)

label7 = Button(root_home, width=20, height=10, bg='white', bd=0)
label7.place(x=220, y=300)

label8 = Button(root_home, width=20, height=10, bg='white', bd=0)
label8.place(x=410, y=300)

label9 = Button(root_home, width=20, height=10, bg='white', bd=0)
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

labelCont = Button(root_home, text='Contest', font=('Open Sans', 11, 'bold'), bd=0, width=10, height=0, bg='white',
                   command=cont)
labelCont.place(x=50, y=230)

labelResearch = Button(root_home, text='Research Paper', font=('Open Sans', 11, 'bold'), bd=0, width=12, height=0,
                       bg='white',command=research)
labelResearch.place(x=235, y=230)

labelNews = Button(root_home, text='NewsFeed', font=('Open Sans', 11, 'bold'), bd=0, width=12, height=0, bg='white')
labelNews.place(x=430, y=230)

labelJob = Button(root_home, text='Job and Internship', font=('Open Sans', 11, 'bold'), bd=0, width=14, height=0,
                  bg='white')
labelJob.place(x=605, y=230)

labelQuiz = Button(root_home, text='Interactive Quiz', font=('Open Sans', 11, 'bold'), bd=0, width=14, height=0,
                   bg='white')
labelQuiz.place(x=40, y=430)

labelClub = Button(root_home, text='Club & Community', font=('Open Sans', 11, 'bold'), bd=0, width=14, height=0,
                   bg='white')
labelClub.place(x=230, y=430)



labelExchange = Button(root_home, text='Study Abroad', font=('Open Sans', 11, 'bold'), bd=0, width=14, height=0,
                   bg='white')
labelExchange.place(x=420, y=430)

labelExchange = Button(root_home, text='Skill Development', font=('Open Sans', 11, 'bold'), bd=0, width=14, height=0,
                   bg='white')
labelExchange.place(x=605, y=430)




root_home.mainloop()
