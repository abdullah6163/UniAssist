import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def clear_fields():
    name_entry.delete(0, tk.END)
    category_combo.set('')
    date_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)

def upload_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        file_label.config(text="File Uploaded: " + file_path)

root = tk.Tk()
root.title("Submit Research Paper")

w = 600
h = 500
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw - w) // 2
y = (sh - h) // 2
root.geometry(f"{w}x{h}+{x}+{y}")

root.configure(bg="#f0f0f0")
root.grid_rowconfigure(7, weight=1)
root.grid_columnconfigure(1, weight=1)

title_label = tk.Label(root, text="Submit Research Paper", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.grid(row=0, column=0, columnspan=2, pady=20)

name_label = tk.Label(root, text="Paper Title:", bg="#f0f0f0")
name_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
name_entry = tk.Entry(root, width=40)
name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

category_label = tk.Label(root, text="Field of Study:", bg="#f0f0f0")
category_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
categories = ["Computer Science", "Physics", "Biology", "Engineering", "Mathematics"]
category_combo = ttk.Combobox(root, values=categories, width=36)
category_combo.grid(row=2, column=1, padx=20, pady=10, sticky="w")

date_label = tk.Label(root, text="Date (YYYY-MM-DD):", bg="#f0f0f0")
date_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
date_entry = tk.Entry(root, width=40)
date_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

author_label = tk.Label(root, text="Author(s):", bg="#f0f0f0")
author_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")
author_entry = tk.Entry(root, width=40)
author_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

file_label = tk.Label(root, text="Upload PDF File:", bg="#f0f0f0")
file_label.grid(row=5, column=0, padx=20, pady=10, sticky="w")
upload_button = tk.Button(root, text="Upload", command=upload_file)
upload_button.grid(row=5, column=1, padx=20, pady=10, sticky="w")

submit_button = tk.Button(root, text="Submit Paper", width=20)
submit_button.grid(row=6, column=0, columnspan=2, pady=20)

clear_button = tk.Button(root, text="Clear Fields", width=20, command=clear_fields)
clear_button.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
