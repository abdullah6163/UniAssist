import tkinter as tk
from tkinter import ttk, messagebox

class SkillDevelopmentPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Skill Development Registration")
        self.master.geometry("600x500+300+80")
        self.master.configure(bg="#f2f2f2")
        self.master.resizable(False, False)

        # Header
        self.header_label = tk.Label(self.master, text="Skill Development Registration Form", font=("Arial", 18, "bold"), bg="#3399ff", fg="white")
        self.header_label.pack(pady=20, fill=tk.X)

        # Form Frame
        self.form_frame = tk.Frame(self.master, bg="#f2f2f2")
        self.form_frame.pack(pady=10, padx=20)

        # Name
        tk.Label(self.form_frame, text="Your Name:", font=("Arial", 12), bg="#f2f2f2", fg="#333333").grid(row=0, column=0, pady=10, sticky="w")
        self.name_entry = tk.Entry(self.form_frame, font=("Arial", 12), width=30)
        self.name_entry.grid(row=0, column=1, pady=10)

        # Age
        tk.Label(self.form_frame, text="Age:", font=("Arial", 12), bg="#f2f2f2", fg="#333333").grid(row=1, column=0, pady=10, sticky="w")
        self.age_entry = tk.Entry(self.form_frame, font=("Arial", 12), width=30)
        self.age_entry.grid(row=1, column=1, pady=10)

        # Select Skill
        tk.Label(self.form_frame, text="Select Skill:", font=("Arial", 12), bg="#f2f2f2", fg="#333333").grid(row=2, column=0, pady=10, sticky="w")
        self.skills = ["Programming", "Data Analysis", "Machine Learning", "Digital Marketing", "Graphic Design"]
        self.skill_menu = ttk.Combobox(self.form_frame, values=self.skills, font=("Arial", 12), width=28)
        self.skill_menu.grid(row=2, column=1, pady=10)
        self.skill_menu.set(self.skills[0])

        # Experience Level
        tk.Label(self.form_frame, text="Experience Level:", font=("Arial", 12), bg="#f2f2f2", fg="#333333").grid(row=3, column=0, pady=10, sticky="w")
        self.experience_levels = ["Beginner", "Intermediate", "Advanced"]
        self.experience_menu = ttk.Combobox(self.form_frame, values=self.experience_levels, font=("Arial", 12), width=28)
        self.experience_menu.grid(row=3, column=1, pady=10)
        self.experience_menu.set(self.experience_levels[0])

        # Email
        tk.Label(self.form_frame, text="Email:", font=("Arial", 12), bg="#f2f2f2", fg="#333333").grid(row=4, column=0, pady=10, sticky="w")
        self.email_entry = tk.Entry(self.form_frame, font=("Arial", 12), width=30)
        self.email_entry.grid(row=4, column=1, pady=10)

        # Preferred Learning Method
        tk.Label(self.form_frame, text="Preferred Learning Method:", font=("Arial", 12), bg="#f2f2f2", fg="#333333").grid(row=5, column=0, pady=10, sticky="w")
        self.learning_methods = ["Online", "In-Person", "Hybrid"]
        self.learning_method_menu = ttk.Combobox(self.form_frame, values=self.learning_methods, font=("Arial", 12), width=28)
        self.learning_method_menu.grid(row=5, column=1, pady=10)
        self.learning_method_menu.set(self.learning_methods[0])

        # Availability
        tk.Label(self.form_frame, text="Availability:", font=("Arial", 12), bg="#f2f2f2", fg="#333333").grid(row=6, column=0, pady=10, sticky="w")
        self.availability_options = ["Weekdays", "Weekends", "Evenings", "Flexible"]
        self.availability_menu = ttk.Combobox(self.form_frame, values=self.availability_options, font=("Arial", 12), width=28)
        self.availability_menu.grid(row=6, column=1, pady=10)
        self.availability_menu.set(self.availability_options[0])

        # Submit Button
        self.submit_button = tk.Button(self.master, text="Register Now", font=("Arial", 14, "bold"), bg="#3399ff", fg="white", command=self.submit_form)
        self.submit_button.pack(pady=20)

    def submit_form(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        skill = self.skill_menu.get()
        experience = self.experience_menu.get()
        email = self.email_entry.get()
        learning_method = self.learning_method_menu.get()
        availability = self.availability_menu.get()

        if not name or not age or not email:
            messagebox.showwarning("Incomplete Form", "Please fill in all fields.")
            return

        # Here, you can add code to save the form data or send it to a server

        messagebox.showinfo("Form Submitted", f"Thank you {name}!\nYou have registered for the {skill} skill development program.")
        self.master.destroy()

def run_skill_development():
    root = tk.Tk()
    app = SkillDevelopmentPage(root)
    root.mainloop()

if __name__ == "__main__":
    run_skill_development()
