import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import threading
import time
import random
import json
import os

class StudentProductivityToolkit:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Productivity Toolkit")
        self.root.geometry("500x400")
        
        self.create_menu()
        self.current_frame = None
        self.load_timer_frame()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        menu_bar.add_command(label="Timer Belajar", command=self.load_timer_frame)
        menu_bar.add_command(label="Catatan Harian", command=self.load_notes_frame)
        menu_bar.add_command(label="To-Do List", command=self.load_todo_frame)
        menu_bar.add_command(label="Motivational Quotes", command=self.load_quote_frame)
        menu_bar.add_command(label="Kalkulator", command=self.load_calculator_frame)
        menu_bar.add_command(label="Keluar", command=self.exit_app)

    def switch_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.destroy()
        self.current_frame = frame_class(self.root)

    def load_timer_frame(self):
        self.switch_frame(TimerFrame)

    def load_notes_frame(self):
        self.switch_frame(NotesFrame)

    def load_todo_frame(self):
        self.switch_frame(ToDoFrame)

    def load_quote_frame(self):
        self.switch_frame(QuoteFrame)

    def load_calculator_frame(self):
        self.switch_frame(CalculatorFrame)

    def exit_app(self):
        if messagebox.askyesno("Keluar", "Yakin ingin keluar dari aplikasi?"):
            self.root.destroy()
            
class QuoteFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Label(self, text="Motivational Quotes", font=("Arial", 16)).grid(row=0, column=0, pady=10)

        self.quote_label = ttk.Label(self, text="", font=("Arial", 12), wraplength=400)
        self.quote_label.grid(row=1, column=0, pady=10)

        ttk.Button(self, text="Tampilkan Kutipan", command=self.show_quote).grid(row=2, column=0, pady=5)



    def show_quote(self):
        quotes = [
            "Believe in yourself!",
            "Keep pushing forward!",
            "Success is the sum of small efforts, repeated day in and day out.",
            "Don’t watch the clock; do what it does. Keep going.",
            "The future depends on what you do today."
        ]
        self.quote_label.config(text=random.choice(quotes))
    
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentProductivityToolkit(root)
    root.mainloop()
