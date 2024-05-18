
import tkinter as tk
from tkinter import messagebox

class ClubCommunityPage:
    def __init__(self, master):
        self.master = master
        self.master.title("Club and Community Page")
        self.master.geometry("600x400")
        self.master.configure(bg="#E6F5FC")  # Set background color

        # Title Label
        tk.Label(self.master, text="Explore Clubs and Communities", font=("Arial", 20, "bold"), bg="#2E8FC2", fg="white").pack(pady=20)

        # Club Buttons
        clubs = ["Programming Club", "Artistic Society", "Sports Club", "Book Club", "Chess Club", "Science Society"]
        for club_name in clubs:
            tk.Button(self.master, text=club_name, font=("Arial", 14), width=20, pady=10, bg="#20C5CA", fg="black",
                      command=lambda name=club_name: self.open_club_page(name)).pack(pady=10)

    def open_club_page(self, club_name):
        # Example function to open specific club page
        if club_name == "Programming Club":
            self.show_club_info(club_name, "Welcome to the Programming Club!")
        elif club_name == "Artistic Society":
            self.show_club_info(club_name, "Explore the Artistic Society!")
        elif club_name == "Sports Club":
            self.show_club_info(club_name, "Join the Sports Club!")
        elif club_name == "Book Club":
            self.show_club_info(club_name, "Discover the Book Club!")
        elif club_name == "Chess Club":
            self.show_club_info(club_name, "Join the Chess Club and sharpen your skills!")
        elif club_name == "Science Society":
            self.show_club_info(club_name, "Explore the wonders of science with the Science Society!")

    def show_club_info(self, club_name, message):
        response = messagebox.askyesno("Club Page", f"{message}\n\nDo you want to join {club_name}?")
        if response:
            # Add logic to handle joining the club
            messagebox.showinfo("Join Club", f"You have joined {club_name}!")
        else:
            messagebox.showinfo("Club Page", f"Explore {club_name} later!")

def run_club():
    root = tk.Tk()
    app = ClubCommunityPage(root)
    root.mainloop()

if __name__ == "__main__":
    run_club()
