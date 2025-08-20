import tkinter as tk
from tkinter import messagebox

def aprovacao():
    try:
        nota = entry_nota.get().replace(",",".")
        nota = float(nota)

        if nota >= 7:
            messagebox.showinfo("Resultado", "VOCÊ PASSOU.")
        elif nota >= 5:
            messagebox.showinfo("Resultado", "VOCÊ ESTA DE RECUPERÇÃO.")
        else:
                messagebox.showinfo("Resultado", "MEUS PESAMES")
    except ValueError:
         messagebox.showerror("Erro", "Digite um número válido para a nota.")

root = tk.Tk()
root.title("Verificação de Aprovação")
root.geometry("400x200")

tk.Label(root, text="Digite sua nota:").pack(pady=5)
entry_nota = tk.Entry(root)
entry_nota.pack(pady=5)

tk.Button(root, text="Verificar", command=aprovacao).pack(pady=10)

root.mainloop()