from tkinter import *
from PIL import Image, ImageTk
import webbrowser

def open_job_internship(url):
    webbrowser.open_new(url)

# Create the root window
root_jobs = Tk()
root_jobs.title('Job and Internship Opportunities')
root_jobs.geometry('1000x600')
root_jobs.configure(bg='#FFFFFF')  # Set background color
root_jobs.resizable(False, False)

def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    photo = ImageTk.PhotoImage(resized_image)
    return photo

# Header
header_label = Label(root_jobs, text="Job and Internship Opportunities", font=('Open Sans', 24, 'bold'), bg="#FFFFFF", fg="#333333", pady=20)
header_label.pack()

# Job and Internship Data
job_internship_data = [
    {"title": "Software Engineer Intern", "url": "https://www.linkedin.com/jobs/software-engineer-intern"},
    {"title": "Marketing Specialist", "url": "https://www.linkedin.com/jobs/marketing-specialist"},
    {"title": "Data Analyst", "url": "https://www.linkedin.com/jobs/data-analyst"},
    {"title": "Business Development Manager", "url": "https://www.linkedin.com/jobs/business-development-manager"}
]

# Display Job and Internship Titles with Apply Now Buttons
for job in job_internship_data:
    frame = Frame(root_jobs, bg="#FFFFFF")
    frame.pack(pady=10, fill=X)  # Use fill=X to expand the frame horizontally

    title_label = Label(frame, text=job["title"], font=('Open Sans', 14, 'bold'), bg="#FFFFFF", fg="#333333")
    title_label.pack(side=LEFT, padx=20)

    apply_button = Button(frame, text="Apply Now", font=('Open Sans', 12, 'bold'), bg='#20C5CA', fg='white', bd=0,
                          command=lambda u=job["url"]: open_job_internship(u))
    apply_button.pack(side=RIGHT, padx=20, ipadx=10, ipady=5)  # Use ipadx and ipady to adjust button size

# Footer
footer_label = Label(root_jobs, text="© Job Portal 2024", font=('Open Sans', 12), bg="#FFFFFF", fg="#333333", pady=10)
footer_label.pack()

# Start the main event loop
root_jobs.mainloop()
