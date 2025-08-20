import tkinter as tk

def abrir_segunda_tela():
    segunda_tela = tk.Toplevel(root)
    segunda_tela.title("segunda janela")
    segunda_tela.geometry("300x200")

    label2 = tk.Label(segunda_tela, text="voce esta aqui", font=("Arial", 12))
    label2.pack(pady=20)

    btn_voltar = tk.Button(segunda_tela, text="fechar", command=segunda_tela.destroy)
    btn_voltar.pack()

root = tk.Tk()
root.title("tela principal")
root.geometry("300x200")

label = tk.Label(root, text="Bem vindo", font=("Arial", 12))
label.pack(pady=20)

btn_ir = tk.Button(root, text="abrir segunda tela", command=abrir_segunda_tela)
btn_ir.pack()

root.mainloop()