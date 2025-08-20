import tkinter as tk
from tkinter import messagebox

senhaS = "1234"


def senha():
    try:
        senha = entry_senha.get().replace(",",".")  

        if senha == senhaS:
            messagebox.showinfo("Resultado", "senha correta")
        else:
                messagebox.showinfo("Resultado", "senha errada")
    except ValueError:
         messagebox.showerror("Erro", "Digite um número válido para a senha.")

root = tk.Tk()
root.title("Verificação de senha")
root.geometry("400x200")

tk.Label(root, text="Digite sua senha:").pack(pady=5)
entry_senha = tk.Entry(root,show="*")
entry_senha.pack(pady=5)

tk.Button(root, text="Verificar", command=senha).pack(pady=10)

root.mainloop()