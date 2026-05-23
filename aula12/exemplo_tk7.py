import tkinter as tk
from datetime import datetime

def atualizar_relogio():
    agora = datetime.now().strftime("%H:%M:%S")
    label.config(text=agora)
    root.after(10000, atualizar_relogio)


root = tk.Tk()
root.title("Relógio com after()")
label = tk.Label(root, font=("Consolas", 32))
label.pack(padx=20, pady=20)
atualizar_relogio()
root.mainloop()