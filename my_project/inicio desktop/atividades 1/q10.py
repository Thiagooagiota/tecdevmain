import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Minha Aplicação Tkinter")

btn3 = tk.Button(root, text="Sair", command=root.quit)
btn3.pack()

root.mainloop()