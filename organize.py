import tkinter as tk
from tkinter import ttk



root = tk.Tk()
root.title("Organize Contest")

w = 600
h = 500
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw - w) // 2
y = (sh - h) // 2
root.geometry(f"{w}x{h}+{x}+{y}")


root.configure(bg="#f0f0f0")
root.grid_rowconfigure(5, weight=1)
root.grid_columnconfigure(1, weight=1)

title_label = tk.Label(root, text="Organize New Contest", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.grid(row=0, column=0, columnspan=2, pady=20)

name_label = tk.Label(root, text="Contest Name:", bg="#f0f0f0")
name_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")
name_entry = tk.Entry(root, width=40)
name_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

category_label = tk.Label(root, text="Category:", bg="#f0f0f0")
category_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")
categories = ["Coding", "Algorithm", "Web Development", "Data Science", "Mathematics"]
category_combo = ttk.Combobox(root, values=categories, width=36)
category_combo.grid(row=2, column=1, padx=20, pady=10, sticky="w")

date_label = tk.Label(root, text="Date (YYYY-MM-DD):", bg="#f0f0f0")
date_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")
date_entry = tk.Entry(root, width=40)
date_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

duration_label = tk.Label(root, text="Duration (hours):", bg="#f0f0f0")
duration_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")
duration_entry = tk.Entry(root, width=40)
duration_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

description_label = tk.Label(root, text="Description:", bg="#f0f0f0")
description_label.grid(row=5, column=0, padx=20, pady=10, sticky="nw")
description_text = tk.Text(root, width=40, height=5)
description_text.grid(row=5, column=1, padx=20, pady=10, sticky="nw")

organize_button = tk.Button(root, text="Organize Contest", width=20)
organize_button.grid(row=6, column=0, columnspan=2, pady=20)

clear_button = tk.Button(root, text="Clear Fields", width=20)
clear_button.grid(row=7, column=0, columnspan=2, pady=10)


root.mainloop()
