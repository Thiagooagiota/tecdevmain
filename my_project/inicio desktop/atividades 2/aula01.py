import tkinter as tk
from tkinter import ttk, messagebox

janela = tk.Tk()
janela.state("zoomed")
janela.title("cadastro cliente")
janela.config(bg='black')

lista = {}

def listar( nome, email, telefone):
    
    lista[nome] = email,telefone




def cadastrar():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    
    if nome and email and telefone:
        entry_nome.delete(0,tk.END)
        entry_email.delete(0,tk.END)
        entry_telefone.delete(0,tk.END)
        messagebox.showinfo('sucesso', "Cliente Cadastrado")
        listar(nome, email, telefone)
    else:
        messagebox.showerror("erro", "preencha todas as informações")
        

frame_dados_clientes = tk.LabelFrame(text= 'Dados do cliente')
frame_dados_clientes.grid()

label_nome = tk.Label(frame_dados_clientes, text= 'nome:')
label_nome.grid(row=0, column=0, padx=5, pady=5)

label_email = tk.Label(frame_dados_clientes, text= 'email:')
label_email.grid(row=1, column=0, padx=5, pady=5)

label_telefone = tk.Label(frame_dados_clientes, text= 'telefone:')
label_telefone.grid(row=2, column=0, padx=5, pady=5)

entry_nome = tk.Entry(frame_dados_clientes)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

entry_email = tk.Entry(frame_dados_clientes)
entry_email.grid(row=1, column=1, padx=5, pady=5)

entry_telefone = tk.Entry(frame_dados_clientes)
entry_telefone.grid(row=2, column=1, padx=5, pady=5)

btn_cadastro = tk.Button(frame_dados_clientes, text= "cadastrar", command=cadastrar)
btn_cadastro.grid(row=3, column= 0)

btn_limpar = tk.Button(frame_dados_clientes, text= "limpar")
btn_limpar.grid(row=3, column= 1)

btn_excluir = tk.Button(frame_dados_clientes, text= "excluir")
btn_excluir.grid(row=3, column= 2, )

btn_desfazer = tk.Button(frame_dados_clientes, text= "desfazer")
btn_desfazer.grid(row=3, column= 3,)

btn_salvar = tk.Button(frame_dados_clientes, text= "salvar")
btn_salvar.grid(row=3, column= 4,)

frame_clientes_cadastrados = tk.LabelFrame(text= 'Dados do cliente')
frame_clientes_cadastrados.grid(padx=10, pady=10)

tree = ttk.Treeview(frame_clientes_cadastrados, columns=('Id','Nome','Email','telefone'),
show= 'headings')
tree.heading('Id', text='Id')
tree.heading('Nome', text='Nome')
tree.heading('Email', text='Email')
tree.heading('telefone', text='telefone')
tree.grid(row=0,column=0)


janela.mainloop()