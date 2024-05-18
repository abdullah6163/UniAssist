# home.py

from tkinter import *
from PIL import Image, ImageTk
import webbrowser
import importlib.util

def open_job_page():
    try:
        spec = importlib.util.spec_from_file_location("job", "job.py")
        job_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(job_module)
        if hasattr(job_module, 'run_job'):
            job_module.run_job()
        else:
            print("run_job function not found in job.py")
    except Exception as e:
        print(f"Error opening job page: {e}")

def research():
    try:
        script_path = "research.py"
        spec = importlib.util.spec_from_file_location("research", script_path)
        research_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(research_module)

        if hasattr(research_module, 'run_research') and callable(getattr(research_module, 'run_research')):
            research_module.run_research()
        else:
            print("run_research function not found or not callable in research.py")
    except Exception as e:
        print(f"Error opening research page: {e}")

def open_contest():
    try:
        script_path = "contest.py"
        spec = importlib.util.spec_from_file_location("contest", script_path)
        contest_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(contest_module)

        if hasattr(contest_module, 'run_contest') and callable(getattr(contest_module, 'run_contest')):
            contest_module.run_contest()
        else:
            print("run_contest function not found or not callable in contest.py")
    except Exception as e:
        print(f"Error opening contest page: {e}")

def open_quiz():
    try:
        script_path = "quiz.py"
        spec = importlib.util.spec_from_file_location("quiz_module", script_path)
        quiz_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(quiz_module)

        if hasattr(quiz_module, 'run_quiz') and callable(getattr(quiz_module, 'run_quiz')):
            quiz_module.run_quiz()
        else:
            print("run_quiz function not found or not callable in quiz.py")
    except Exception as e:
        print(f"Error opening quiz page: {e}")

def newsfeed_page():
    try:
        script_path = "newsfeed.py"
        spec = importlib.util.spec_from_file_location("newsfeed", script_path)
        newsfeed_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(newsfeed_module)

        if hasattr(newsfeed_module, 'run_newsfeed') and callable(getattr(newsfeed_module, 'run_newsfeed')):
            newsfeed_module.run_newsfeed()
        else:
            print("run_newsfeed function not found or not callable in newsfeed.py")
    except Exception as e:
        print(f"Error opening newsfeed page: {e}")

def open_news():
    try:
        script_path = "newsfeed.py"
        spec = importlib.util.spec_from_file_location("newsfeed", script_path)
        newsfeed_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(newsfeed_module)

        if hasattr(newsfeed_module, 'run_newsfeed') and callable(getattr(newsfeed_module, 'run_newsfeed')):
            newsfeed_module.run_newsfeed()
        else:
            print("run_newsfeed function not found or not callable in newsfeed.py")
    except Exception as e:
        print(f"Error opening newsfeed page: {e}")

def open_club():
    try:
        script_path = "club.py"
        spec = importlib.util.spec_from_file_location("club_module", script_path)
        club_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(club_module)

        if hasattr(club_module, 'run_club') and callable(getattr(club_module, 'run_club')):
            club_module.run_club()
        else:
            print("run_club function not found or not callable in club.py")
    except Exception as e:
        print(f"Error opening club page: {e}")

def study():
    try:
        script_path = "abroad.py"
        spec = importlib.util.spec_from_file_location("abroad_module", script_path)
        abroad_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(abroad_module)

        if hasattr(abroad_module, 'run_study_abroad') and callable(getattr(abroad_module, 'run_study_abroad')):
            abroad_module.run_study_abroad()
        else:
            print("run_study_abroad function not found or not callable in abroad.py")
    except Exception as e:
        print(f"Error opening abroad page: {e}")

def skill_dev():
    try:
        script_path = "skill.py"
        spec = importlib.util.spec_from_file_location("skill_module", script_path)
        skill_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(skill_module)

        if hasattr(skill_module, 'run_skill_development') and callable(getattr(skill_module, 'run_skill_development')):
            skill_module.run_skill_development()
        else:
            print("run_skill_development function not found or not callable in skill.py")
    except Exception as e:
        print(f"Error opening skill page: {e}")

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
root_home.title('Home Page')

label1 = Label(root_home, width=120, height=5, bg='#2E8FC2')
label1.place(x=0, y=0)

home_path = 'image/home-button.png'
homepic = resize_image(home_path, 40, 40)
homeL = Label(root_home, image=homepic, bg='#2E8FC2')
homeL.place(x=10, y=20)

heading = Label(root_home, width=30, text='Welcome To UniConnect', font=('Open Sans', 22, 'bold'), bg='#2E8FC2', fg='white')
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

newsfeed_path = 'image/success.png'
newsfeedImg = resize_image(newsfeed_path, 80, 80)
CL = Label(root_home, image=newsfeedImg, bg='white')
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

labelCont = Button(root_home, text='Contest', font=('Open Sans', 11, 'bold'), bd=0, width=10, height=0, bg='white', command=open_contest)
labelCont.place(x=50, y=230)

labelResearch = Button(root_home, text='Research Paper', font=('Open Sans', 11, 'bold'), bd=0, width=12, height=0, bg='white', command=research)
labelResearch.place(x=235, y=230)

labelNews = Button(root_home, text='NewsFeed', font=('Open Sans', 11, 'bold'), bd=0, width=12, height=0, bg='white', command=open_news)
labelNews.place(x=430, y=230)

labelJob = Button(root_home, text='Job and Internship', font=('Open Sans', 11, 'bold'), bd=0, width=14, height=0, bg='white', command=open_job_page)
labelJob.place(x=605, y=230)

labelQuiz = Button(root_home, text='Interactive Quiz', font=('Open Sans', 11, 'bold'), bd=0, width=14, height=0, bg='white', command=open_quiz)
labelQuiz.place(x=40, y=430)

labelClub = Button(root_home, text='Club & Community', font=('Open Sans', 11, 'bold'), bd=0, width=14, height=0, bg='white', command=open_club)
labelClub.place(x=230, y=430)

labelExchange = Button(root_home, text='Study Abroad', font=('Open Sans', 11, 'bold'), bd=0, width=14, height=0, bg='white',command=study)
labelExchange.place(x=420, y=430)

labelExchange1 = Button(root_home, text='Skill Development', font=('Open Sans', 11, 'bold'), bd=0, width=14, height=0, bg='white',command=skill_dev)
labelExchange1.place(x=605, y=430)

root_home.mainloop()
