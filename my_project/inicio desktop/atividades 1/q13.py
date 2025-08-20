import tkinter as tk
from tkinter import messagebox

def numero():
    try:
        numero = entry_numero.get().replace(",",".")
        numero = float(numero)

        if numero >= 1:
            messagebox.showinfo("Resultado", "Seu numero é positivo.")
        elif numero == 0:
            messagebox.showinfo("Resultado", "seu numero é 0 e não se categoriza nem como positivo e nem como negativo.")
        else:
                messagebox.showinfo("Resultado", "seu numero é negativo")
    except ValueError:
         messagebox.showerror("Erro", "Digite um número válido para a numero.")

root = tk.Tk()
root.title("Verificação de Numero")
root.geometry("400x200")

tk.Label(root, text="Digite seu numero:").pack(pady=5)
entry_numero = tk.Entry(root)
entry_numero.pack(pady=5)

tk.Button(root, text="Verificar", command=numero).pack(pady=10)

root.mainloop()