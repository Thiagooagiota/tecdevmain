import customtkinter as ctk
from tkinter import messagebox

#COFIGURAR O TEMA
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

#Janela Principal

root = ctk.CTk()
root.title('tela de login')
root.geometry("450x350")


#rotulo e campo de usuario

label_user = ctk.CTkLabel(root, text="Usuario: ")
label_user.pack(pady=(20,5))
entry_user = ctk.CTkEntry(root, placeholder_text= "Digite seu usuario")
entry_user.pack(pady=5)

#campo de senha

label_senha = ctk.CTkLabel(root, text="Senha")
label_senha.pack(pady=(20,5))
entry_senha = ctk.CTkEntry(root, placeholder_text= "Digite seu usuario")
entry_senha.pack(pady=5)

#frame para os botoes lado a lado

frame_botoes = ctk.CTkFrame(root)
frame_botoes.pack(pady=20)

btn_entrar = ctk.CTkButton(frame_botoes, text="Entrar")
btn_entrar.grid(row=0, column=0, padx=10)

btn_cancelar = ctk.CTkButton(frame_botoes, text="cancelar", fg_color="blue", hover_color="red")
btn_cancelar.grid(row=0, column=0, padx=10)

root.mainloop()
