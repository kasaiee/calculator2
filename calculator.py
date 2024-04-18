import tkinter as tk
from tkinter import ttk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)

entry = tk.Entry(root, width=20, font=("Helvetica", 16), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, column) in buttons:
    button = ttk.Button(root, text=text, style="TButton", command=lambda text=text: button_click(text))
    button.grid(row=row, column=column, padx=5, pady=5, sticky="nsew")

clear_button = ttk.Button(root, text="C", style="TButton", command=button_clear)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

equal_button = ttk.Button(root, text="=", style="TButton", command=button_equal)
equal_button.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky="nsew")

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
