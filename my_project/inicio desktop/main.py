import tkinter as tk
from PIL import Image, ImageTk

janela = tk.Tk()
janela.title("teste")
janela.geometry("400x400")

img = Image.open("casa.png")
img = img.resize((200,200))
img = ImageTk.PhotoImage(img)

imagens = tk.Label(janela, image=img)
imagens.pack()


rotulo1 = tk.Label(janela, text="login")
rotulo1.pack(pady=5)
caixa1 = tk.Entry(janela,width=30)
caixa1.pack(pady=5)

rotulo2 = tk.Label(janela, text="senha")
rotulo2.pack(pady=5)
caixa2 = tk.Entry(janela,width=30)
caixa2.pack(pady=5)

botao1 = tk.Button(janela, text="entrar")
botao1.pack(pady=10)

botao1 = tk.Button(janela, text="cancelar")
botao1.pack(pady=5)

janela.mainloop()