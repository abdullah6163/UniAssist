import tkinter as tk
from PIL import Image, ImageTk
import webbrowser



def open_news(url):
    webbrowser.open_new(url)  

root_news = tk.Tk()
w = 800
h = 600
sw = root_news.winfo_screenwidth()
sh = root_news.winfo_screenheight()

x = (sw // 2) - (w // 2)
y = (sh // 2) - (h // 2)
root_news.geometry(f"{w}x{h}+{x}+{y}")
root_news.configure(bg="#F0F0F0")
root_news.resizable(0, 0)
root_news.title('Newsfeed')

def resize_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height))
    photo = ImageTk.PhotoImage(resized_image)
    return photo


header_frame = tk.Frame(root_news, bg="#2E8FC2", height=80)
header_frame.pack(fill=tk.X)

header_label = tk.Label(header_frame, text="Newsfeed", font=('Open Sans', 24, 'bold'), bg="#2E8FC2", fg="white")
header_label.pack(pady=20)

# News headlines and URLs (Replace with actual news URLs)
news_headlines = [
    "Dhaka University Receives International Recognition",
    "BUET Ranked Among Top Engineering Universities",
    "AIUB Launches New Research Center"
]

news_urls = [
    "https://www.du.ac.bd/news",
    "https://www.buet.ac.bd/news",
    "https://www.aiub.edu/news"
]


for i, (headline, url) in enumerate(zip(news_headlines, news_urls), start=1):
    news_frame = tk.Frame(root_news, bg="#FFFFFF", bd=2, relief=tk.RIDGE)
    news_frame.place(x=50, y=150 + (i - 1) * 120, width=700, height=100)

    headline_label = tk.Label(news_frame, text=headline, font=('Open Sans', 14, 'bold'), bg="#FFFFFF", fg="#333333")
    headline_label.pack(pady=10, padx=20, anchor="w", fill=tk.X)

    read_button = tk.Button(news_frame, text="Read", font=('Open Sans', 12, 'bold'), bg='#20C5CA', fg='black',
                            command=lambda url=url: open_news(url))
    read_button.pack(side=tk.BOTTOM, padx=20, pady=10)

footer_frame = tk.Frame(root_news, bg="#2E8FC2", height=50)
footer_frame.pack(fill=tk.X, side=tk.BOTTOM)




root_news.mainloop()
