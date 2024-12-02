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





class CalculatorFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(fill="both", expand=True, padx=10, pady=10)

        ttk.Label(self, text="Kalkulator", font=("Arial", 16)).grid(row=0, column=0, columnspan=4, pady=10)

        self.entry = ttk.Entry(self, font=("Arial", 14), justify="right")
        self.entry.grid(row=1, column=0, columnspan=4, sticky="we", padx=5, pady=5)

        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('C', 5, 0), ('0', 5, 1), ('=', 5, 2), ('+', 5, 3),
        ]

        for (text, row, col) in buttons:
            ttk.Button(self, text=text, command=lambda t=text: self.on_button_click(t)).grid(
                row=row, column=col, padx=5, pady=5, sticky="nsew"
            )

        for i in range(6):
            self.rowconfigure(i, weight=1)
        for i in range(4):
            self.columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.entry.delete(0, tk.END)
        elif char == "=":
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception:
                messagebox.showerror("Error", "Ekspresi tidak valid")
        else:
            self.entry.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentProductivityToolkit(root)
    root.mainloop()
