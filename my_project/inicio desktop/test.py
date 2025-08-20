import tkinter as tk
from tkinter import ttk

#criar janela principal

janela = tk.Tk()
janela.title("Formulario de Cadastro")
janela.geometry("600x450")
janela.configure(bg="#ffffff") # fundo

style = ttk.Style()
style.theme_use("clam") #tema mais moderno
style.configure('Tlabel', font=('Arial', 10), background='#ffffff')
style.configure('TEntry', padding=5)
style.configure('TButton', font=('Arial', 11, 'bold'), padding=6,
                foreground='#ffffff', bg='blue')

style.map("TButton", background=[('active', "#0D25B1")]) #hover

#titulo do formulario

titulo = tk.Label(
    janela,
    text='cadastro de usuario',
    font=('arial', 16),
    bg='#ffffff',
    fg="#000000"
)
titulo.grid(row=0,column=0,columnspan=4,pady=20) 

ttk.Label(janela, text='NOME:').grid(row=1,column=1,padx=15,pady=8,sticky='w')
caixa_nome = ttk.Entry(janela, width=40)
caixa_nome.grid(row=1,column=2,padx=15,pady=8,sticky='ew')

ttk.Label(janela, text='EMAIL:').grid(row=2,column=1,padx=15,pady=8,sticky='w')
caixa_snome = ttk.Entry(janela, width=40)
caixa_snome.grid(row=2,column=2,padx=15,pady=8,sticky='ew')

ttk.Label(janela, text='TELEFONE:').grid(row=3,column=1,padx=15,pady=8,sticky='w')
caixa_telefone = ttk.Entry(janela, width=40)
caixa_telefone.grid(row=3,column=2,padx=15,pady=8,sticky='ew')

ttk.Label(janela, text='ENDEREÇO:').grid(row=4,column=1,padx=15,pady=8,sticky='w')
caixa_endereco = ttk.Entry(janela, width=40)
caixa_endereco.grid(row=4,column=2,padx=15,pady=8,sticky='ew')

frame_botoes = tk.Frame(janela, bg="#ffffff")
frame_botoes.grid(row=6,column=0,columnspan=4,pady=20)

botao_salvar = ttk.Button(frame_botoes, text="salvar")
botao_salvar.pack(side="left", padx=10)

botao_limpar = ttk.Button(frame_botoes, text="limpar")
botao_limpar.pack(side="left", padx=10)

janela.grid_columnconfigure(0,weight=1)
janela.grid_columnconfigure(1,weight=0)
janela.grid_columnconfigure(2,weight=1)
janela.grid_columnconfigure(3,weight=1)

janela.mainloop()