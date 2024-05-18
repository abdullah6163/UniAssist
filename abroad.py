import tkinter as tk
from tkinter import ttk, messagebox

class StudyAbroadPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Study Abroad Registration")
        self.master.geometry("600x600+300+80")
        self.master.configure(bg="#e6f7ff")
        self.master.resizable(False, False)

        self.header_label = tk.Label(self.master, text="Study Abroad Registration Form", font=("Arial", 18, "bold"), bg="#4da6ff", fg="white")
        self.header_label.pack(pady=20, fill=tk.X)

        self.form_frame = tk.Frame(self.master, bg="#e6f7ff")
        self.form_frame.pack(pady=10, padx=20)

        # Name
        tk.Label(self.form_frame, text="Your Name:", font=("Arial", 12), bg="#e6f7ff", fg="#333333").grid(row=0, column=0, pady=10, sticky="w")
        self.name_entry = tk.Entry(self.form_frame, font=("Arial", 12), width=30)
        self.name_entry.grid(row=0, column=1, pady=10)

        # Age
        tk.Label(self.form_frame, text="Age:", font=("Arial", 12), bg="#e6f7ff", fg="#333333").grid(row=1, column=0, pady=10, sticky="w")
        self.age_entry = tk.Entry(self.form_frame, font=("Arial", 12), width=30)
        self.age_entry.grid(row=1, column=1, pady=10)

        # Select University
        tk.Label(self.form_frame, text="Select University:", font=("Arial", 12), bg="#e6f7ff", fg="#333333").grid(row=2, column=0, pady=10, sticky="w")
        self.universities = ["National University of Singapore", "Tsinghua University", "Peking University", "University of Tokyo", "Seoul National University"]
        self.university_var = tk.StringVar(self.master)
        self.university_var.set(self.universities[0])
        self.university_menu = ttk.Combobox(self.form_frame, values=self.universities, font=("Arial", 12), width=28)
        self.university_menu.grid(row=2, column=1, pady=10)

        # Select Program
        tk.Label(self.form_frame, text="Select Program:", font=("Arial", 12), bg="#e6f7ff", fg="#333333").grid(row=3, column=0, pady=10, sticky="w")
        self.programs = ["Bachelor", "Masters", "PhD", "More"]
        self.program_var = tk.StringVar(self.master)
        self.program_var.set(self.programs[0])
        self.program_menu = ttk.Combobox(self.form_frame, values=self.programs, font=("Arial", 12), width=28)
        self.program_menu.grid(row=3, column=1, pady=10)

        # Select CGPA
        tk.Label(self.form_frame, text="Select your current CGPA:", font=("Arial", 12), bg="#e6f7ff", fg="#333333").grid(row=4, column=0, pady=10, sticky="w")
        self.cgpa_options = ["4.0", "3.5", "3.0", "2.5", "2.0", "N/A"]
        self.cgpa_var = tk.StringVar(self.master)
        self.cgpa_var.set(self.cgpa_options[0])
        self.cgpa_menu = ttk.Combobox(self.form_frame, values=self.cgpa_options, font=("Arial", 12), width=28)
        self.cgpa_menu.grid(row=4, column=1, pady=10)

        # IELTS Score
        tk.Label(self.form_frame, text="IELTS Score:", font=("Arial", 12), bg="#e6f7ff", fg="#333333").grid(row=5, column=0, pady=10, sticky="w")
        self.ielts_entry = tk.Entry(self.form_frame, font=("Arial", 12), width=30)
        self.ielts_entry.grid(row=5, column=1, pady=10)

        # Email
        tk.Label(self.form_frame, text="Email:", font=("Arial", 12), bg="#e6f7ff", fg="#333333").grid(row=6, column=0, pady=10, sticky="w")
        self.email_entry = tk.Entry(self.form_frame, font=("Arial", 12), width=30)
        self.email_entry.grid(row=6, column=1, pady=10)

        # Submit Button
        self.submit_button = tk.Button(self.master, text="Apply Now", font=("Arial", 14, "bold"), bg="#4da6ff", fg="white", command=self.submit_form)
        self.submit_button.pack(pady=20)

    def submit_form(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        university = self.university_menu.get()
        program = self.program_menu.get()
        cgpa = self.cgpa_menu.get()
        ielts = self.ielts_entry.get()
        email = self.email_entry.get()

        if not name or not age or not email:
            messagebox.showwarning("Incomplete Form", "Please fill in all fields.")
            return

        # Here, you can add code to save the form data or send it to a server

        messagebox.showinfo("Form Submitted", f"Thank you {name}!\nYour application for the {program} program at {university} has been submitted.")
        self.master.destroy()

def run_study_abroad():
    root = tk.Tk()
    app = StudyAbroadPage(root)
    root.mainloop()

if __name__ == "__main__":
    run_study_abroad()
