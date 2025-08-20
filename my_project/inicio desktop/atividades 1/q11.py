import tkinter as tk
from tkinter import messagebox
import webbrowser

def verificar_idade():
    try:
        idade = int(entry_idade.get())
        if idade >= 18:
            messagebox.showinfo("Resultado", "Você é maior de idade.")
        else:
            messagebox.showinfo("Resultado", "Você é menor de idade.")
            messagebox.showinfo("resultadO","redirecionando para fotos de gatinho")
            webbrowser.open("https://www.google.com/search?sca_esv=2388371dc08fac3b&udm=2&fbs=AIIjpHxX5k-tONtMCu8aDeA7E5WMdDwGSuc8eBkl8hX51y2q6-r6qOmgvFs8yhx59bJgnXQRW0CpTUrikAvoMvruBQ5EkjQ7FupD3cXkpY3rXiGQpuuHaxh9SG2qSTWBGtc3GjuXqY-mnyyIsBMUI_GA5YrJRFSns4DTixoF0dNLDA9VtDUVR93ccGvPI0DV_Y3YyQtg13F0lmm3hoX51ElGvCiSOlM_yA&q=fotos+de+gatinho&sa=X&ved=2ahUKEwj1_v6iw5qPAxXjr5UCHbpzDw0QtKgLegQIERAB&biw=1912&bih=956")
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para a idade.")

    

root = tk.Tk()
root.title("Verificação de Idade")
root.geometry("400x200")

tk.Label(root, text="Digite sua idade:").pack(pady=5)
entry_idade = tk.Entry(root)
entry_idade.pack(pady=5)

tk.Button(root, text="Verificar", command=verificar_idade).pack(pady=10)

root.mainloop()