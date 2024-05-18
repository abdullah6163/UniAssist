import tkinter as tk
from tkinter import messagebox

class InteractiveProgrammingQuiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Interactive Programming Quiz")
        self.master.geometry("600x400+300+80")
        self.master.configure(bg="#f0f8ff")
        self.master.resizable(False, False)

        self.questions = [
            {
                "question": "What does HTML stand for?",
                "options": ["Hyper Text Markup Language", "Hyperlinks and Text Markup Language", "Home Tool Markup Language", "High Tech Markup Language"],
                "correct_answer": "Hyper Text Markup Language"
            },
            {
                "question": "Which programming language is known for its use in web development?",
                "options": ["Java", "Python", "JavaScript", "C++"],
                "correct_answer": "JavaScript"
            },
            {
                "question": "What is the output of '3 + 4 * 2' in Python?",
                "options": ["14", "11", "10", "Error"],
                "correct_answer": "11"
            },
            {
                "question": "What is the name of the version control system created by Linus Torvalds?",
                "options": ["Git", "SVN", "Mercurial", "Perforce"],
                "correct_answer": "Git"
            },
            {
                "question": "What does the acronym 'OOP' stand for in programming?",
                "options": ["Object-Oriented Programming", "Object Overload Process", "Optimal Object Parsing", "Operation Oriented Protocol"],
                "correct_answer": "Object-Oriented Programming"
            },
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": ["def", "function", "define", "func"],
                "correct_answer": "def"
            }
        ]

        self.current_question_index = 0
        self.score = 0

        self.question_label = tk.Label(self.master, text="", font=("Arial", 16, "bold"), bg="#f0f8ff", fg="#333333", wraplength=500, justify="center")
        self.question_label.pack(pady=20)

        self.option_buttons = []
        button_colors = ["#ff9999", "#99ff99", "#9999ff", "#ffcc99"]
        for i in range(4):
            button = tk.Button(self.master, text="", font=("Arial", 12, "bold"), width=40, bg=button_colors[i], fg="#333333", command=lambda idx=i: self.check_answer(idx))
            button.pack(pady=10)
            self.option_buttons.append(button)

        self.next_question()

    def next_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])
            for i in range(4):
                self.option_buttons[i].config(text=question_data["options"][i])
            self.current_question_index += 1
        else:
            self.show_result()

    def check_answer(self, selected_index):
        question_data = self.questions[self.current_question_index - 1]
        correct_answer = question_data["correct_answer"]
        selected_answer = question_data["options"][selected_index]

        if selected_answer == correct_answer:
            self.score += 1

        if self.current_question_index < len(self.questions):
            self.next_question()
        else:
            self.show_result()

    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"You scored {self.score}/{len(self.questions)}")
        self.master.destroy()

def run_quiz():
    root = tk.Tk()
    app = InteractiveProgrammingQuiz(root)
    root.mainloop()

if __name__ == "__main__":
    run_quiz()
