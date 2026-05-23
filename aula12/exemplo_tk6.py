import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Dashboard com abas")

notebook = ttk.Notebook(root)
aba1 = ttk.Frame(notebook)
aba2 = ttk.Frame(notebook)
notebook.add(aba1, text="Principal")
notebook.add(aba2, text="Sobre")
notebook.pack(expand=True, fill='both')

ttk.Label(aba1, text="Conteúdo da aba principal").pack(padx=10, pady=10)
ttk.Label(aba2, text="Informações sobre o sistema").pack(padx=10, pady=10)

root.mainloop()