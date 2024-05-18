from tkinter import *
from tkinter import messagebox
import webbrowser
import importlib.util



def org():
    try:
        script_path = "organize.py"
        spec = importlib.util.spec_from_file_location("organize", script_path)
        organize_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(organize_module)

        if hasattr(organize_module, 'run_organize') and callable(getattr(organize_module, 'run_organize')):
            organize_module.run_organize()
        else:
            print("run_organize function not found or not callable in organize.py")

    except Exception as e:
        print(f"Error opening organize page: {e}")
def register_success():
    messagebox.showinfo("Registration", "Successfully Registered")

root_cont = Tk()
w = 780
h = 530
sw = root_cont.winfo_screenwidth()
sh = root_cont.winfo_screenheight()

x = (sw // 2) - (w // 2)
y = (sh // 2) - (h // 2)
root_cont.geometry(f"{w}x{h}+{x}+{y}")
root_cont.configure(bg="#E6F5FC")
root_cont.resizable(0, 0)
root_cont.title('organize Page')

label1 = Label(root_cont, width=120, height=5, bg='#2E8FC2')
label1.place(x=0, y=0)

heading = Label(root_cont, width=30, text='Contest', font=('Open Sans', 22, 'bold'), bg='#2E8FC2', fg='white')
heading.place(x=100, y=20)

organizes = [
    ("Diu Coding Challenge", "15 May 2024", "running", "https://codeforces.com/organizes"),
    ("Aiub Programming organize", "15 May 2024", "running", "https://atcoder.jp/organizes"),
    ("Du Beginner organize", "15 May 2024", "running", "https://toph.co/c/du-beginner-organize"),
    ("Algorithm Hackathon", "15 May 2024", "upcoming", "https://codeforces.com/organizes"),
    ("Data Science Competition", "15 May 2024", "upcoming", "https://atcoder.jp/organizes")
]

y_offset = 100
for organize_name, date, status, url in organizes:
    organize_label = Label(root_cont, width=60, text=f"{organize_name} ({status.capitalize()}, {date}, Duration: 2 hours)",
                          font=('Open Sans', 12), bg='#E6F5FC', fg='black')
    organize_label.place(x=60, y=y_offset)

    if status == "running":
        button_text = "Join"
    else:
        button_text = "Register"

    action_button = Button(root_cont, width=8, height=0, text=button_text, font=('Open Sans', 8), bg='#20C5CA', fg='black',
                           command=lambda link=url: webbrowser.open_new(link))
    action_button.place(x=650, y=y_offset)

    y_offset += 30

heading6 = Label(root_cont, width=60, text='Want to organize a organize?',
                 font=('Open Sans', 12, 'bold'), bg='#E6F5FC', fg='black')
heading6.place(x=80, y=450)

button6 = Button(root_cont, width=8, height=0, text="Click Here", font=('Open Sans', 12, 'bold'), bg='#E6F5FC', fg='blue', bd=0,command=org)
button6.place(x=500, y=448)

root_cont.mainloop()
