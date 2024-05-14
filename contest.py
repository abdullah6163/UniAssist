import tkinter as tk

def display_contests(parent, contests, row_start):
    for i, contest in enumerate(contests, start=row_start):
        label_text = f"{contest['name']} ({contest['type']} - {contest['date']})"
        label = tk.Label(parent, text=label_text, width=50, bg='white',anchor="w", pady=5, font=("Arial", 12))
        label.grid(row=i, column=0, padx=20, pady=5, sticky="w")

        if contest['type'] == 'Running':
            join_button = tk.Button(parent, text="Join", width=8,bg='white', command=lambda name=contest['name']: join_contest(name))
            join_button.grid(row=i, column=1, padx=10, pady=5)
        elif contest['type'] == 'Upcoming':
            register_button = tk.Button(parent, text="Register", width=8,bg='white', command=lambda name=contest['name']: register_contest(name))
            register_button.grid(row=i, column=1, padx=10, pady=5)

def join_contest(contest_name):
    print(f"Joining {contest_name}...")
def register_contest(contest_name):
    print(f"Registering for {contest_name}...")

running_contests = [
    {"name": "Diu Coding Challenge", "type": "Running", "date": "May 15, 2024"},
    {"name": "BracU Hackathon Contest", "type": "Running", "date": "June 1, 2024"}
]

upcoming_contests = [
    {"name": "Data Science Competition", "type": "Upcoming", "date": "July 10, 2024"},
    {"name": "Aust Programming Contest", "type": "Upcoming", "date": "August 5, 2024"}
]

root = tk.Tk()
root.title("Contest Page")

w = 800
h = 500
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw - w) // 2
y = (sh - h) // 2
root.geometry(f"{w}x{h}+{x}+{y}")
root.configure(bg="#E1F6F7")

running_label = tk.Label(root, text="Running Contests", font=("Arial", 16, "bold"),bg='white')
running_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")
display_contests(root, running_contests, row_start=1)


upcoming_label = tk.Label(root, text="Upcoming Contests", font=("Arial", 16, "bold"),bg='white')
upcoming_label.grid(row=len(running_contests)+2, column=0, padx=20, pady=20, sticky="w")
display_contests(root, upcoming_contests, row_start=len(running_contests)+3)


root.mainloop()
