import tkinter as tk
from tkinter import messagebox

precos = {1: ["pizza",30.00],
          2: ["hamburguer", 25.00],
          3: ["refrigerante", 5.00]}


def produto():
    try:
        produto = int(entry_produto.get())  

        if produto in precos:
            nome, preco = precos[produto]
            messagebox.showinfo("valor", f"{nome}: {preco:.2f}")
        else:
            messagebox.showerror("ERRO","produto invalido")
            
    except ValueError:
         messagebox.showerror("Erro", "Digite um número válido para a produto.")

root = tk.Tk()
root.title("Verificação de produto")
root.geometry("400x200")

produtos = ""

for codigo, (nome,preco) in precos.items():
    produtos += f"\n{codigo}:{nome}"

tk.Label(root, text="Digite seu produto:").pack(pady=5)
tk.Label(root,text= produtos).pack(pady=5)
entry_produto = tk.Entry(root)
entry_produto.pack(pady=5)

tk.Button(root, text="Verificar", command=produto).pack(pady=10)

root.mainloop()