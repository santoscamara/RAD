import tkinter as tk
from tkinter import ttk

class AppMeses:
    def __init__(self, root):
        self.root = root
        self.root.geometry('250x120')
        self.root.title("Exemplo Combobox")
        tk.Label(self.root, text = "Selecione um Mês: ").pack(pady=5)
        self.meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        self.combo = ttk.Combobox(self.root, values=self.meses, state="readon1y")
        self.combo.pack(pady=5)
        self.combo.current(0)
        self.combo.bind("<<ComboboxSelected>>", self.selecionar_mes)

    def selecionar_mes(self, event):
        selecao = self.combo.get()
        print(f"Mês escolhido: {selecao}")
root = tk.Tk()
AppMeses(root)
root.mainloop()